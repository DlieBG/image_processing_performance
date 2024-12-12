# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
import math

def rgb_to_hsv(rgb_pixel: tuple[int, int, int]) -> tuple[int, int, int]:
    """ Convert an RGB pixel to an HSV pixel.
        Algorithm reference from http://alvyray.com/Papers/CG/color78.pdf.
        Algorithm reference from https://www.rapidtables.com/convert/color/rgb-to-hsv.html.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            rgb_pixel (tuple[int, int, int]): RGB pixel.

        Returns:
            tuple[int, int, int]: HSV pixel.
    """
    # Get the red, green, and blue values of the RGB pixel in the range [0, 1].
    red = rgb_pixel[0] / 255
    green = rgb_pixel[1] / 255
    blue = rgb_pixel[2] / 255

    # Get the maximum and minimum values of the RGB pixel.
    max_value = max(red, green, blue)
    min_value = min(red, green, blue)

    # Get the delta of the maximum and minimum values.
    delta = max_value - min_value

    # Calculate the hue value of the HSV pixel.
    if delta == 0:
        # All RGB values are the same, so the hue is undefined.
        hue = 0
    elif max_value == red:
        # Red is the maximum value.
        # Calculate the hue based on the green and blue values.
        hue = 60 * (((green - blue) / delta) % 6)
    elif max_value == green:
        # Green is the maximum value.
        # Calculate the hue based on the blue and red values.
        hue = 60 * (((blue - red) / delta) + 2)
    else:
        # Blue is the maximum value.
        # Calculate the hue based on the red and green values.
        hue = 60 * (((red - green) / delta) + 4)

    # Calculate the saturation value of the HSV pixel.
    if max_value == 0:
        # The maximum value is zero, so the saturation is zero.
        saturation = 0
    else:
        # Calculate the saturation based on the delta.
        saturation = delta / max_value

    # Calculate the value value of the HSV pixel.
    value = max_value

    # Create a new HSV pixel and return it.
    return (
        hue,
        saturation,
        value,
    )

def rgb_to_hsv_image(rgb_image: tuple[int, int, list[tuple[int, int, int]]]) -> tuple[int, int, list[tuple[int, int, int]]]:
    """ Convert an RGB image to an HSV image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            rgb_image (tuple[int, int, list[tuple[int, int, int]]]): RGB image.

        Returns:
            tuple[int, int, list[tuple[int, int, int]]]: HSV image.
    """
    # Create a new HSV image and return it.
    # Use list comprehension to convert each RGB pixel to an HSV pixel.
    return (
        rgb_image[0],
        rgb_image[1],
        [
            rgb_to_hsv(rgb_pixel) 
                for rgb_pixel in rgb_image[2]
        ],
    )

def weighted_hsv_distance(pixel1: tuple[int, int, int], pixel2: tuple[int, int, int], hue_weight: float = 1, saturation_weight: float = 1, value_weight: float = 1) -> float:
    """ Calculate the weighted HSV distance between two HSV pixels.
        Algorithm reference from https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a451df3b73675133370e8d3238643a4c6106cbd0.
        Facing hue wrapping issue, the algorithm is adjusted to consider the shortest distance between two hue values.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            pixel1 (tuple[int, int, int]): First HSV pixel.
            pixel2 (tuple[int, int, int]): Second HSV pixel.
            hue_weight (float): Weight for the hue distance.
            saturation_weight (float): Weight for the saturation distance.
            value_weight (float): Weight for the value distance.

        Returns:
            float: Weighted HSV distance in the range [0, 255].
    """
    # Calculate the cyclic hue distance.
    delta_hue = min(abs(pixel1[0] - pixel2[0]), 360 - abs(pixel1[0] - pixel2[0])) / 360

    # Calculate the saturation and value distance.
    delta_saturation = abs(pixel1[1] - pixel2[1])
    delta_value = abs(pixel1[2] - pixel2[2])

    # Calculate the weighted HSV distance and return it.
    return math.sqrt(hue_weight * delta_hue ** 2 + saturation_weight * delta_saturation ** 2 + value_weight * delta_value ** 2) * 255
