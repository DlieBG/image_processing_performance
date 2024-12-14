# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.slow.utils.image import open_project_image, save_project_image
from src.slow.utils.hsv import rgb_to_hsv_image, weighted_hsv_distance
from src.slow.models.image import Pixel
from src.slow.utils.log import log
from pathlib import Path

WHITE_PIXEL = Pixel.white()
BLACK_PIXEL = Pixel.black()

def background_subtraction(threshold: float, hsv: bool, reference_image_path: Path, input_image_path: Path, output_image_path: Path):
    """ Apply Background Subtraction on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            hsv (bool): Flag to convert the image to HSV.
            reference_image_path (Path): Reference path for image file.
            input_image_path (Path): Input path for image file.
            output_image_path (Path): Output path for image file.

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
    if reference_image.width != image.width or reference_image.height != image.height:
        raise ValueError('The reference image and the input image must have the same dimensions.')

    # Convert the reference image and the input image to HSV if the flag is set.
    # This provides better time tracking for the algorithm.
    if hsv:
        hsv_reference_image = rgb_to_hsv_image(
            rgb_image=reference_image,
        )
        hsv_image = rgb_to_hsv_image(
            rgb_image=image,
        )
        log('finish hsv conversion')

    # Iterate over each pixel in the image.
    for row in range(image.height):
        for column in range(image.width):
            # Use the HSV pixels if the flag is set.
            # Otherwise, use the RGB pixels.
            if hsv:
                hsv_reference_pixel = hsv_reference_image.pixels[row][column]
                hsv_pixel = hsv_image.pixels[row][column]

                # Calculate the difference between the HSV pixels.
                difference = weighted_hsv_distance(
                    pixel1=hsv_reference_pixel,
                    pixel2=hsv_pixel,
                    hue_weight=.6,
                    saturation_weight=.6,
                    value_weight=.1,
                )
            else:
                reference_pixel = reference_image.pixels[row][column]
                pixel = image.pixels[row][column]

                # Calculate the difference between the RGB pixels.
                difference = abs(reference_pixel.red - pixel.red) / 3 + abs(reference_pixel.green - pixel.green) / 3 + abs(reference_pixel.blue - pixel.blue) / 3

            # If the difference is greater than the threshold, set the pixel to white.
            # Otherwise, set the pixel to black.
            if difference > threshold:
                image.pixels[row][column] = WHITE_PIXEL
            else:
                image.pixels[row][column] = BLACK_PIXEL
    log('finish background subtraction')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=image,
    )
    log('finish save image')
