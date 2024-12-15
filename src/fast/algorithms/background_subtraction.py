# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.fast.utils.image import open_project_image, save_project_image
from src.fast.utils.hsv import rgb_to_hsv_pixel, weighted_hsv_distance
from src.parser.utils.log import log
from pathlib import Path

WHITE_PIXEL = (255, 255, 255)
BLACK_PIXEL = (0, 0, 0)

def background_subtraction(threshold: float, hsv: bool, hsv_weights: tuple[float, float, float], reference_image_path: Path, input_image_path: Path, output_image_path: Path):
    """ Apply Background Subtraction on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            hsv (bool): Flag to convert the image to HSV.
            hsv_weights (tuple[float, float, float]): Weights for the HSV values.
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
    image = open_project_image(
        image_path=input_image_path,
    )
    log('finish preprocessing')

    # Check if the reference image and the input image have the same dimensions.
    if reference_image[0] != image[0] or reference_image[1] != image[1]:
        raise ValueError('The reference image and the input image must have the same dimensions.')

    # Iterate over each pixel in the image.
    for index in range(image[0] * image[1]):
        if hsv:
            # Convert the RGB pixels to HSV without saving the whole image.
            hsv_reference_pixel = rgb_to_hsv_pixel(
                rgb_pixel=reference_image[2][index],
            )
            hsv_pixel = rgb_to_hsv_pixel(
                rgb_pixel=image[2][index],
            )

            # Calculate the difference between the HSV pixels.
            difference = weighted_hsv_distance(
                pixel1=hsv_reference_pixel,
                pixel2=hsv_pixel,
                weights=hsv_weights,
            )
        else:
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
    log('finish postprocessing')
