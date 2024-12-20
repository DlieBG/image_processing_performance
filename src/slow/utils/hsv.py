# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.slow.models.hsv import HSVImage, HSVPixel
from src.slow.models.image import Image, Pixel
import math

def rgb_to_hsv_pixel(rgb_pixel: Pixel) -> HSVPixel:
    """ Convert an RGB pixel to an HSV pixel.
        Algorithm reference from http://alvyray.com/Papers/CG/color78.pdf.
        Algorithm reference from https://www.rapidtables.com/convert/color/rgb-to-hsv.html.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            rgb_pixel (Pixel): RGB pixel.

        Returns:
            HSVPixel: HSV pixel.
    """
    # Get the red, green, and blue values of the RGB pixel in the range [0, 1].
    red = rgb_pixel.red / 255
    green = rgb_pixel.green / 255
    blue = rgb_pixel.blue / 255

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
    return HSVPixel(
        hue=hue,
        saturation=saturation,
        value=value,
    )

def rgb_to_hsv_image(rgb_image: Image) -> HSVImage:
    """ Convert an RGB image to an HSV image.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            rgb_image (Image): RGB image.

        Returns:
            HSVImage: HSV image.
    """
    # Get the width and height of the RGB image.
    width = rgb_image.width
    height = rgb_image.height

    # Get the HSV pixels of the RGB image pixels.
    hsv_pixels = [
        [
            rgb_to_hsv_pixel(
                rgb_pixel=pixel,
            )
                for pixel in row
        ]
            for row in rgb_image.pixels
    ]

    # Create a new HSV image and return it.
    return HSVImage(
        width=width,
        height=height,
        pixels=hsv_pixels,
    )

def weighted_hsv_distance(pixel1: HSVPixel, pixel2: HSVPixel, weights: tuple[float, float, float]) -> float:
    """ Calculate the weighted HSV distance between two HSV pixels.
        Algorithm reference from https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a451df3b73675133370e8d3238643a4c6106cbd0.
        Facing hue wrapping issue, the algorithm is adjusted to consider the shortest distance between two hue values.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            pixel1 (HSVPixel): First HSV pixel.
            pixel2 (HSVPixel): Second HSV pixel.
            weights (tuple[float, float, float]): Weights for the HSV distance calculation.

        Returns:
            float: Weighted HSV distance in the range [0, 255].
    """
    # Calculate the cyclic hue distance.
    delta_hue = min(abs(pixel1.hue - pixel2.hue), 360 - abs(pixel1.hue - pixel2.hue)) / 360

    # Calculate the saturation and value distance.
    delta_saturation = abs(pixel1.saturation - pixel2.saturation)
    delta_value = abs(pixel1.value - pixel2.value)

    # Calculate the weighted HSV distance and return it.
    return math.sqrt(weights[0] * delta_hue ** 2 + weights[1] * delta_saturation ** 2 + weights[2] * delta_value ** 2) * 255
