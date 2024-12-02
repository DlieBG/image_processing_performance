# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.algorithms.background_subtraction import background_subtraction as background_subtraction_algorithm
from pathlib import Path
import click

@click.group()
def cli():
    pass

@cli.command(
    name='background_subtraction',
    help='Background Subtraction on a set of images.'
)
@click.option(
    '--threshold',
    '-t',
    type=float,
    default=7.0,
    show_default=True,
    help='Threshold value for background subtraction.'
)
@click.argument(
    'reference_image_file',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
    required=True,
)
@click.argument(
    'image_files',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
    required=True,
    nargs=-1,
)
def background_subtraction(threshold: float, reference_image_file: str, image_files: tuple[str, ...]):
    """ Background Subtraction on a set of images.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            image_files (tuple[str, ...]): List of image files.
    """
    reference_image_path = Path(reference_image_file)

    for image_file in image_files:
        # Convert the image file to a Path object.
        image_path = Path(image_file)

        background_subtraction_algorithm(
            threshold=threshold,
            reference_image_path=reference_image_path,
            input_image_path=image_path,
            output_image_path=image_path.parent / f'background_subtraction_{image_path.name}',
        )
