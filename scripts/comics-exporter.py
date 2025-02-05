#!/usr/bin/python3

import json
import os
import sqlite3
from pathlib import Path
import sys

USAGE = """Usage: python comics-exporter.py <filename>

    filename - fixed_dino_comics.json
"""


def create_database(filename):
    # Connect to SQLite database
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    # comics table is simple
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comics (
        id INTEGER PRIMARY KEY,
        title TEXT,
        url TEXT
    )
    """)

    # omic_panels table holds one panel per row
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comic_panels (
        comic_id INTEGER,
        panel INTEGER,
        panel_content TEXT,
        FOREIGN KEY (comic_id) REFERENCES comics (id),
        PRIMARY KEY (comic_id, panel)
    )
    """)

    conn.commit()
    return conn, cursor


def import_comics(file_path: Path):
    # Check if file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(f"The file {file_path} was not found")

    # Read JSON file
    with open(file_path, "r") as file:
        comics_data = json.load(file)
        print(f"Data from {file_path} import successfully")

    filename = os.path.splitext(os.path.basename(file_path))[0]
    database_filename = f"{filename}.db"

    # Connect to database
    conn, cursor = create_database(database_filename)

    try:
        for comic in comics_data:
            # ignore comics not written by Ryan North
            if "guest comic" in comic["meta"]:
                continue
            # Insert into comics table
            cursor.execute(
                """
            INSERT OR REPLACE INTO comics (id, title, url)
            VALUES (?, ?, ?)
            """,
                (comic["id"], comic["title"], comic["url"]),
            )

            for i, text in enumerate(comic["text"]):
                cursor.execute(
                    """
                INSERT OR REPLACE INTO comic_panels (comic_id, panel, panel_content)
                VALUES (?, ?, ?)
                """,
                    (comic["id"], i, text),
                )

        conn.commit()
        print(f"Database {database_filename} written successfully")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        conn.rollback()

    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    filename = sys.argv[1]
    import_comics(filename)
