# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from setuptools import find_packages, setup

setup(
    name='image_processing_performance',
    version='0.1.0',
    description='Image Processing Performance Python Tools',
    author='Benedikt Schwering',
    author_email='bes9584@thi.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'pillow',
        'click',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'ipp_python = src.__main__:cli',
        ],
    },
)
