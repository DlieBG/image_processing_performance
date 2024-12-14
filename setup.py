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
    version='0.1.3',
    description='Image Processing Performance Python Tools',
    author='Benedikt Schwering',
    author_email='bes9584@thi.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'openpyxl',
        'pillow',
        'pandas',
        'click',
        'numpy',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'ipp_slow = src.slow.main:cli',
            'ipp_fast = src.fast.main:cli',
            'ipp_numpy = src.numpy.main:cli',
            'ipp_parser = src.parser.main:cli',
        ],
    },
)
