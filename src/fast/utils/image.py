# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.fast.models.image import Image
from src.fast.utils.log import log
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
    log('finish open pil image')

    # Convert the image to RGB if it is not already.
    # This is necessary because the image is not always in RGB format.
    # For example, the image could be in RGBA with an alpha channel in PNG format.
    pil_image = pil_image.convert('RGB')
    log('finish convert pil image')

    # Create a new project image and return it.
    return Image(
        width=pil_image.width,
        height=pil_image.height,
        pixels=pil_image.getdata(),
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
    log('finish create pil image')

    # Put the data of the project image into the PIL image.
    pil_image.putdata(
        data=project_image.pixels,
    )
    log('finish put data to pil image')
    
    # Save the PIL image to the file.
    pil_image.save(
        fp=image_path,
    )
    log('finish save pil image')
