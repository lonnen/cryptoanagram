#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages

with open(os.path.join('cryptoanagram', '__init__.py'), 'rt') as f:
    version = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M).group(1)

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cryptoanagram',
    version=version,
    description='a cryptoanagram solver utility for comic 1663',
    long_description=readme,
    author='Lonnen',
    author_email='chris.lonnen@gmail.com',
    url='https://github.com/lonnen/cryptoanagram',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[], # use pip -r requirements.txt && pip -r requirements-dev.txt
    include_package_data=True,
    package_dir={
        'cryptoanagram': 'cryptoanagram'
    }
)