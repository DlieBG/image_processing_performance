# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.utils.image import open_project_image, save_project_image
from pathlib import Path

def background_subtraction(delta: float, input_path: Path, output_path: Path):
    """ Background Subtraction on a set of images.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            delta (float): Threshold value for background subtraction.
            input_path (Path): Input path for image files.
            output_path (Path): Output path for image files.
    """
    project_image = open_project_image(
        image_path=input_path,
    )

    # Todo: Implement Background Subtraction Algorithm

    save_project_image(
        image_path=output_path,
        project_image=project_image,
    )
