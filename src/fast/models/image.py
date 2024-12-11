# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from pydantic import BaseModel

class Image(BaseModel):
    """ Image class for the project.
    
        Author:
            Benedikt Schwering <bes9584@thi.de>
    """
    width: int
    height: int
    pixels: list[tuple[int, int, int]]
