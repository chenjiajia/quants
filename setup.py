#!/usr/bin/env python
# coding=utf-8

import os

from setuptools import setup, find_packages

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def _parse_requirement_file(path):
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    return requirements


def get_install_requires():
    requirement_file = os.path.join(THIS_FOLDER, "requirements.txt")
    return _parse_requirement_file(requirement_file)

setup(
    name="quants",
    version="0.1.0",
    description="stock quant utils",
    packages=find_packages(exclude=("tests", "tests.*")),
    author="chenjiajia",
    author_email="chenjiajia1@gmail.com",
    maintainer="chenjiajia",
    maintainer_email="chenjiajia1@gmail.com",
    package_data={'': ['*.*']},
    long_description="",
    long_description_content_type='text/markdown',
    install_requires=get_install_requires(),
    zip_safe=False,
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)