# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.slow.utils.image import open_project_image, save_project_image, get_neighbor_pixels
from src.slow.models.image import Pixel
from src.slow.utils.log import log
from pathlib import Path

WHITE_PIXEL = Pixel.white()
BLACK_PIXEL = Pixel.black()

def dilate(radius: int, input_image_path: Path, output_image_path: Path):
    """ Apply Dilation on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            radius (int): Radius value for dilation.
            input_image_path (Path): Input path for image file.
            output_image_path (Path): Output path for image file.
    """
    # Open the input image.
    input_image = open_project_image(
        image_path=input_image_path,
    )
    log('finish open image')

    # Create a copy of the input input image as output image.
    output_image = input_image.model_copy(
        deep=True,
    )
    log('finish create output image')

    # Iterate over each pixel in the image.
    for row in range(input_image.height):
        for column in range(input_image.width):
            # Get the neighbor pixels of the current pixel.
            neighbor_pixels = get_neighbor_pixels(
                image=input_image,
                row=row,
                column=column,
                radius=radius,
            )

            # Check if any neighbor pixels is white.
            if any(
                pixel.is_white()
                    for pixel in neighbor_pixels
            ):
                # Set the pixel to white.
                output_image.pixels[row][column] = WHITE_PIXEL
            else:
                # Set the pixel to black.
                output_image.pixels[row][column] = BLACK_PIXEL
    log('finish dilate')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=output_image,
    )
    log('finish save image')
