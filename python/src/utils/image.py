# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.models.image import Image, Pixel
from PIL import Image as PILImage
from pathlib import Path

def open_project_image(image_path: Path) -> Image:
    """ Open a project image from a file.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            image_path (Path): Path to the image.

        Returns:
            Image: Project image.
    """
    # Open the image with the PIL library.
    pil_image = PILImage.open(
        fp=image_path,
        mode='r',
    )

    # Convert the image to RGB if it is not already.
    # This is necessary because the image is not always in RGB format.
    # For example, the image could be in RGBA with an alpha channel in PNG format.
    pil_image = pil_image.convert('RGB')

    # Get the width and height of the image.
    width, height = pil_image.size

    # Get the flat data of the image.
    flat_data = list(pil_image.getdata())

    # Convert the flat data to a list of pixels.
    flat_pixels = [
        Pixel(
            red=flat_pixel[0],
            green=flat_pixel[1],
            blue=flat_pixel[2],
        )
            for flat_pixel in flat_data
    ]

    # Convert the pixels to a two dimensional list.
    pixels = [
        flat_pixels[i:i + width]
            for i in range(0, len(flat_pixels), width)
    ]

    # Create a new project image and return it.
    return Image(
        width=width,
        height=height,
        pixels=pixels,
    )

def save_project_image(image_path: Path, project_image: Image):
    """ Save a project image to a file.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            image_path (Path): Path to the image.
            project_image (Image): Project image.
    """
    # Create a new PIL image with the same width and height as the project image.
    pil_image = PILImage.new(
        mode='RGB',
        size=(project_image.width, project_image.height),
    )

    # Get the flat pixels of the project image two dimensional pixels.
    flat_pixels = [
        pixel
            for row in project_image.pixels
                for pixel in row
    ]

    # Get the flat data of the project image flat pixels.
    flat_data = [
        (pixel.red, pixel.green, pixel.blue)
            for pixel in flat_pixels
    ]

    # Put the flat data into the PIL image.
    pil_image.putdata(
        data=flat_data,
    )

    # Save the PIL image to the file.
    pil_image.save(
        fp=image_path,
    )
