# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from pydantic import BaseModel

class Pixel(BaseModel):
    """ Pixel class for the project.

        Author:
            Benedikt Schwering <bes9584@thi.de>
    """
    red: int
    green: int
    blue: int

    @staticmethod
    def white() -> 'Pixel':
        """ Initialize a white pixel.
        
            Author:
                Benedikt Schwering <bes9584@thi.de>
            
            Returns:
                Pixel: White pixel.
        """
        return Pixel(
            red=255,
            green=255,
            blue=255,
        )

    @staticmethod
    def black() -> 'Pixel':
        """ Initialize a black pixel.
        
            Author:
                Benedikt Schwering <bes9584@thi.de>
            
            Returns:
                Pixel: Black pixel.
        """
        return Pixel(
            red=0,
            green=0,
            blue=0,
        )

    def is_white(self) -> bool:
        """ Check if the pixel is white.

            Author:
                Benedikt Schwering <bes9584@thi.de>

            Returns:
                bool: True if the pixel is white, False otherwise.
        """
        return self.red == 255 and self.green == 255 and self.blue == 255
    
    def is_black(self) -> bool:
        """ Check if the pixel is black.

            Author:
                Benedikt Schwering <bes9584@thi.de>

            Returns:
                bool: True if the pixel is black, False otherwise.
        """
        return self.red == 0 and self.green == 0 and self.blue == 0

class Image(BaseModel):
    """ Image class for the project.

        Author:
            Benedikt Schwering <bes9584@thi.de>
    """
    width: int
    height: int
    pixels: list[list[Pixel]]
