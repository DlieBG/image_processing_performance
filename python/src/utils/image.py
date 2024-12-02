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
            red=flat_data[i],
            green=flat_data[i + 1],
            blue=flat_data[i + 2],
        )
            for i in range(
                start=0,
                stop=len(flat_data),
                step=3,
            )
    ]

    # Convert the pixels to a two dimensional list.
    pixels = [
        flat_pixels[i:i + width]
            for i in range(
                start=0,
                stop=len(flat_pixels),
                step=width,
            )
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
    pass
