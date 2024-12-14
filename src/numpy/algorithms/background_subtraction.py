# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.numpy.utils.image import open_project_image, save_project_image
from concurrent.futures import ThreadPoolExecutor
from src.numpy.utils.log import log
import numpy.typing as npt
from pathlib import Path
import numpy as np
import cv2

WHITE_PIXEL = [255, 255, 255]

def __process_chunk(threshold: float, hsv: bool, reference_image_chunk, image_chunk) -> npt.NDArray[np.uint8]:
    """ Process a chunk of an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            hsv (bool): Flag to convert the image to HSV.
            reference_image_chunk (np.array): Chunk of the reference image.
            image_chunk (np.array): Chunk of the image.

        Returns:
            np.array: Processed chunk of the image.
    """
    if hsv:
        # Convert the image chanks to HSV.
        # HUE values are in the range [0, 180].
        # SATURATION and VALUE values are in the range [0, 255].
        reference_image_chunk = cv2.cvtColor(reference_image_chunk, cv2.COLOR_RGB2HSV)
        image_chunk = cv2.cvtColor(image_chunk, cv2.COLOR_RGB2HSV)

        # Calculate the difference between the HSV pixels.
        # Convert the pixel to int16 to avoid overflow.
        difference = np.abs(image_chunk.astype(np.int16) - reference_image_chunk.astype(np.int16))

        # Handle the HUE channel separately.
        # Calculate the difference between the HUE pixels.
        hue_difference = np.minimum(
            np.abs(difference[:, :, 0]),
            180 - np.abs(difference[:, :, 0]),
        )

        # Apply the weights to the differences.
        pixel_differences = (
            1.25 * hue_difference +
            1 * difference[:, :, 1] +
            .5 * difference[:, :, 2]
        )
    else:
        # Calculate the difference between the RGB pixels.
        # Convert the pixel to int16 to avoid overflow.
        difference = np.abs(image_chunk.astype(np.int16) - reference_image_chunk.astype(np.int16))

        # Calculate the mean of the differences along the color channels.
        pixel_differences = difference.mean(
            axis=2,
        )

    # Create a binary mask based on the threshold.
    binary_mask = pixel_differences > threshold

    # Create a new black image chunk with the same dimensions as the input image.
    result_chunk = np.zeros_like(image_chunk)

    # Set the pixels to white where the binary mask is True.
    result_chunk[binary_mask] = WHITE_PIXEL

    # Return the processed chunk.
    return result_chunk

def background_subtraction(threshold: float, hsv: bool, threads: int, reference_image_path: Path, input_image_path: Path, output_image_path: Path):
    """ Apply Background Subtraction on an image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            threshold (float): Threshold value for background subtraction.
            hsv (bool): Flag to convert the image to HSV.
            threads (int): Number of threads to use for parallel processing.
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
    if reference_image.shape != image.shape:
        raise ValueError('The reference image and the input image must have the same dimensions.')

    # Split the image and reference image into chunks along the height (axis=0).
    image_chunks = np.array_split(image, threads, axis=0)
    reference_image_chunks = np.array_split(reference_image, threads, axis=0)

    # Process each chunk in parallel.
    with ThreadPoolExecutor(
        max_workers=threads,
    ) as executor:
        results = list(
            executor.map(
                __process_chunk,
                [threshold] * threads,
                [hsv] * threads,
                reference_image_chunks,
                image_chunks
            )
        )

    # Combine the chunks back into a single image.
    processed_image = np.vstack(results)
    log('finish background subtraction')

    # Save the image to the output path.
    save_project_image(
        image_path=output_image_path,
        project_image=processed_image,
    )
    log('finish save image')
