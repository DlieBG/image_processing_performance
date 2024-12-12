# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.fast.utils.image import open_project_image, save_project_image, create_project_image, any_neighbors_equal_pixel
from src.fast.utils.log import log
from pathlib import Path

WHITE_PIXEL = (255, 255, 255)
BLACK_PIXEL = (0, 0, 0)

def erode(radius: int, input_image_path: Path, output_image_path: Path):
    """ Apply Erosion on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            radius (int): Radius value for erosion.
            input_path (Path): Input path for image file.
            output_path (Path): Output path for image file.
    """
    # Open the input image.
    input_image = open_project_image(
        image_path=input_image_path,
    )
    log('finish open image')

    # Create an white project image as output image.
    output_image = create_project_image(
        width=input_image[0],
        height=input_image[1],
        init_pixel=WHITE_PIXEL,
    )
    log('finish create output image')

    # Iterate over each pixel in the image.
    for index in range(input_image[0] * input_image[1]):
        # Check if any neighbor pixels is black.
        if any_neighbors_equal_pixel(
            image=input_image,
            radius=radius,
            index=index,
            check_pixel=BLACK_PIXEL,
        ):
            # Set the pixel to black.
            output_image[2][index] = BLACK_PIXEL
    log('finish erode')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=output_image,
    )
    log('finish save image')
