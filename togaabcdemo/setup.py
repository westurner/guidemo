#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./togaabcdemo/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='togaabcdemo',
    version=version,
    description='A demo app with Toga (and briefcase)',
    long_description=long_description,
    author='Wes Turner',
    author_email='wes.turner@gmail.com',
    license='GNU General Public License v2 (GPLv2)',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Toga ABC Demo',
            'bundle': 'org.westurner.togaabcdemo'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
                'toga-cocoa==0.3.0.dev9',
            ]
        },
        'linux': {
            'app_requires': [
                'toga-gtk==0.3.0.dev9',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winforms==0.3.0.dev9',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
                'toga-ios==0.3.0.dev9',
            ]
        },
        'android': {
            'app_requires': [
                'toga-android==0.3.0.dev9',
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
                'toga-django==0.3.0.dev9',
            ]
        },
    }
)
