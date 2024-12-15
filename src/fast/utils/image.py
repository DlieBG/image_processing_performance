# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.parser.utils.log import log
from PIL import Image as PILImage
from pathlib import Path

def open_project_image(image_path: Path) -> tuple[int, int, list[tuple[int, int, int]]]:
    """ Open a project image from a file.
    
        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            image_path (Path): Path to the image.

        Returns:
            (int, int, list[tuple[int, int, int]]): Width, height and pixels of the project image.
    """
    # Open the image with the PIL library.
    pil_image = PILImage.open(
        fp=image_path,
        mode='r',
    )
    log('finish open pil image')

    # Convert the image to RGB if it is not already.
    # This is necessary because the image is not always in RGB format.
    # For example, the image could be in RGBA with an alpha channel in PNG format.
    pil_image = pil_image.convert('RGB')
    log('finish convert pil image')

    # Create a new project image and return it.
    return (
        pil_image.width,
        pil_image.height,
        list(pil_image.getdata()),
    )

def save_project_image(image_path: Path, project_image: tuple[int, int, list[tuple[int, int, int]]]):
    """ Save a project image to a file.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            image_path (Path): Path to the image.
            project_image (tuple[int, int, list[tuple[int, int, int]]]): Project image.
    """
    # Create a new PIL image with the same width and height as the project image.
    pil_image = PILImage.new(
        mode='RGB',
        size=(project_image[0], project_image[1]),
    )
    log('finish create pil image')

    # Put the data of the project image into the PIL image.
    pil_image.putdata(
        data=project_image[2],
    )
    log('finish put data to pil image')
    
    # Save the PIL image to the file.
    pil_image.save(
        fp=image_path,
    )
    log('finish save pil image')

def create_project_image(width: int, height: int, init_pixel: tuple[int, int, int]) -> tuple[int, int, list[tuple[int, int, int]]]:
    """ Create an empty project image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            width (int): Width of the image.
            height (int): Height of the image.
            init_pixel (tuple[int, int, int]): Initial pixel value.

        Returns:
            (int, int, list[tuple[int, int, int]]): Width, height and pixels of the project image.
    """
    return (
        width,
        height,
        [init_pixel] * width * height,
    )

def any_neighbors_equal_pixel(image: tuple[int, int, list[tuple[int, int, int]]], radius: int, index: int, check_pixel: tuple[int, int, int]) -> bool:
    """ Check if any neighbors of a pixel are equal to a given check pixel.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            image (tuple[int, int, list[tuple[int, int, int]]]): Reference Image.
            radius (int): Radius value.
            index (int): Index of the pixel.
            check_pixel (tuple[int, int, int]): Given check pixel.

        Returns:
            bool: True if any neighbor is equal, False otherwise.
    """
    # Get the width and height of the image.
    width = image[0]
    height = image[1]

    # Get the x and y position of the pixel.
    x, y = index % width, index // width

    # Get the x and y range for the neighbors.
    x_range = range(max(x - radius, 0), min(x + radius + 1, width))
    y_range = range(max(y - radius, 0), min(y + radius + 1, height))

    # Check if any neighbor is equal to the check pixel.
    for x_neighbor in x_range:
        for y_neighbor in y_range:
            if image[2][y_neighbor * width + x_neighbor] == check_pixel:
                return True

    return False
