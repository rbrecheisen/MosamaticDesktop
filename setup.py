#!/usr/bin/env python

import os

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        requirements.append(line)

setup_requirements = []

test_requirements = []

with open('VERSION') as f:
    VERSION = f.read()

setup(
    author="Ralph Brecheisen",
    author_email='r.brecheisen@maastrichtuniversity.nl',
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    # package_dir={
    #     'src': 'src/mosamaticdesktop',
    # },
    # package='mosamaticdesktop',
    packages=find_packages(include=[
        'mosamaticdesktop', 
        'mosamaticdesktop.*', 
        'mosamaticdesktop.aiservice',
        'mosamaticdesktop.data',
        'mosamaticdesktop.data.models',
        'mosamaticdesktop.tasks',
        'mosamaticdesktop.tasks.*',
        'mosamaticdesktop.widgets',
        'mosamaticdesktop.widgets.*',
    ]),
    include_package_data=True,
    package_data={
        'mosamaticdesktop': ['scripts/*', 'VERSION', 'GIT_COMMIT_ID'],
    },
    description="Desktop tool for analyzing medical images",
    install_requires=requirements,
    license="MIT license",
    keywords='mosamaticdesktop',
    name='mosamaticdesktop',
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'mosamatic-desktop=mosamaticdesktop.main:main',
        ],
    },
    version=VERSION,
    zip_safe=False,
)