# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.numpy.utils.image import open_project_image, save_project_image
from src.parser.utils.log import log
from pathlib import Path
import numpy as np

BLACK_PIXEL = [0, 0, 0]

def erode(radius: int, input_image_path: Path, output_image_path: Path):
    """ Apply Erosion on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            radius (int): Radius value for erosion.
            input_image_path (Path): Input path for image file.
            output_image_path (Path): Output path for image file.
    """
    # Open the input image.
    input_image = open_project_image(
        image_path=input_image_path,
    )

    # Create a white project image as output image.
    output_image = np.full_like(
        input_image,
        255,
        dtype=np.uint8,
    )
    log('finish preprocessing')

    # Convert the image to a boolean mask where black pixels are True.
    mask = np.all(
        input_image == BLACK_PIXEL,
        axis=-1,
    )

    # Pad the mask to handle border conditions.
    padded_mask = np.pad(
        mask,
        pad_width=radius,
        mode='constant',
        constant_values=False,
    )

    # Use a sliding window to check the neighborhood for black pixels.
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            # Shift the padded mask and accumulate.
            # Set the eroded mask to True if any pixel in the neighborhood is black.
            mask |= padded_mask[
                radius + dy:radius + dy + mask.shape[0],
                radius + dx:radius + dx + mask.shape[1],
            ]

    # Where the eroded mask is true, set the output image pixels to black.
    output_image[mask] = BLACK_PIXEL
    log('finish erode')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=output_image,
    )
    log('finish postprocessing')
