# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cryptoanagram',
    version='0.1.0',
    description='a cryptoanagram solver utility for comic 1663',
    long_description=readme,
    author='Lonnen',
    author_email='chris.lonnen@gmail.com',
    url='https://github.com/lonnen/cryptoanagram',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

