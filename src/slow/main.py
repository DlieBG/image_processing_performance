# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.slow.algorithms.background_subtraction import background_subtraction as background_subtraction_algorithm
from src.slow.algorithms.dilate import dilate as dilate_algorithm
from src.slow.algorithms.erode import erode as erode_algorithm
from pathlib import Path
import click

@click.group()
def cli():
    """ Image Processing Performance - Slow Implementation

        Author:
            Benedikt Schwering <bes9584@thi.de>
    """
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
@click.option(
    '--hsv',
    '-h',
    is_flag=True,
    default=False,
    show_default=True,
    help='HSV mode for background subtraction.'
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
def background_subtraction(threshold: float, hsv: bool, reference_image_file: str, image_files: tuple[str, ...]):
    """ Background Subtraction on a set of images.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            image_files (tuple[str, ...]): List of image files.
    """
    # Convert the reference image file to a Path object.
    reference_image_path = Path(reference_image_file)

    for image_file in image_files:
        # Convert the image file to a Path object.
        image_path = Path(image_file)

        # Perform background subtraction on the image.
        background_subtraction_algorithm(
            threshold=threshold,
            hsv=hsv,
            reference_image_path=reference_image_path,
            input_image_path=image_path,
            output_image_path=image_path.parent / f'background_subtraction_{image_path.name}',
        )

@cli.command(
    name='erode',
    help='Erode a set of images.'
)
@click.option(
    '--radius',
    '-r',
    type=int,
    default=2,
    show_default=True,
    help='Radius value for erosion.'
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
def erode(radius: int, image_files: tuple[str, ...]):
    """ Erode a set of images.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            radius (int): Radius value for erosion.
            image_files (tuple[str, ...]): List of image files.
    """
    for image_file in image_files:
        # Convert the image file to a Path object.
        image_path = Path(image_file)

        # Perform erosion on the image.
        erode_algorithm(
            radius=radius,
            input_image_path=image_path,
            output_image_path=image_path.parent / f'erode_{image_path.name}',
        )

@cli.command(
    name='dilate',
    help='Dilate a set of images.'
)
@click.option(
    '--radius',
    '-r',
    type=int,
    default=2,
    show_default=True,
    help='Radius value for dilation.'
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
def dilate(radius: int, image_files: tuple[str, ...]):
    """ Dilate a set of images.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            radius (int): Radius value for dilation.
            image_files (tuple[str, ...]): List of image files.
    """
    for image_file in image_files:
        # Convert the image file to a Path object.
        image_path = Path(image_file)

        # Perform dilation on the image.
        dilate_algorithm(
            radius=radius,
            input_image_path=image_path,
            output_image_path=image_path.parent / f'dilate_{image_path.name}',
        )
