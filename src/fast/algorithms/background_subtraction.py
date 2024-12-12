# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.fast.utils.image import open_project_image, save_project_image
from src.fast.utils.log import log
from pathlib import Path

WHITE_PIXEL = (255, 255, 255)
BLACK_PIXEL = (0, 0, 0)

def background_subtraction(threshold: float, hsv: bool, reference_image_path: Path, input_image_path: Path, output_image_path: Path):
    """ Apply Background Subtraction on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            input_path (Path): Input path for image file.
            output_path (Path): Output path for image file.

        Raises:
            ValueError: If the reference image and the input image do not have the same dimensions.
    """
    # Open the reference image and the input image.
    reference_image = open_project_image(
        image_path=reference_image_path,
    )
    log('finish open reference image')

    image = open_project_image(
        image_path=input_image_path,
    )
    log('finish open image')

    # Check if the reference image and the input image have the same dimensions.
    if reference_image[0] != image[0] or reference_image[1] != image[1]:
        raise ValueError('The reference image and the input image must have the same dimensions.')

    # Iterate over each pixel in the image.
    for index in range(image[0] * image[1]):
        reference_pixel = reference_image[2][index]
        pixel = image[2][index]

        # Calculate the difference between the RGB pixels.
        difference = abs(reference_pixel[0] - pixel[0]) / 3 + abs(reference_pixel[1] - pixel[1]) / 3 + abs(reference_pixel[2] - pixel[2]) / 3

        # If the difference is greater than the threshold, set the pixel to white.
        # Otherwise, set the pixel to black.
        if difference > threshold:
            image[2][index] = WHITE_PIXEL
        else:
            image[2][index] = BLACK_PIXEL
    log('finish background subtraction')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=image,
    )
    log('finish save image')
