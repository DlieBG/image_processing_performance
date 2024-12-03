# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.utils.image import open_project_image, save_project_image
from src.models.image import Pixel
from pathlib import Path

WHITE_PIXEL = Pixel.white()
BLACK_PIXEL = Pixel.black()

def background_subtraction(threshold: float, reference_image_path: Path, input_image_path: Path, output_image_path: Path):
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
    image = open_project_image(
        image_path=input_image_path,
    )

    # Check if the reference image and the input image have the same dimensions.
    if reference_image.width != image.width or reference_image.height != image.height:
        raise ValueError('The reference image and the input image must have the same dimensions.')

    # Iterate over each pixel in the image.
    for row in range(image.height):
        for column in range(image.width):
            reference_pixel = reference_image.pixels[row][column]
            pixel = image.pixels[row][column]

            # Calculate the difference between the pixel values.
            difference = abs(reference_pixel.red - pixel.red) / 3 + abs(reference_pixel.green - pixel.green) / 3 + abs(reference_pixel.blue - pixel.blue) / 3

            # If the difference is greater than the threshold, set the pixel to white.
            # Otherwise, set the pixel to black.
            if difference > threshold:
                image.pixels[row][column] = WHITE_PIXEL
            else:
                image.pixels[row][column] = BLACK_PIXEL

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=image,
    )
