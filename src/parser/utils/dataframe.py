# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from pathlib import Path
import pandas as pd
import re

def convert_to_dataframe(time_tracking_file: Path) -> pd.DataFrame:
    """ Convert time tracking file to pandas DataFrame.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            time_tracking_file (Path): Time tracking file to convert.
    
        Returns:
            pd.DataFrame: Time tracking file as pandas DataFrame.
    """
    # Initialize empty lists
    timestamps = []
    layers = []
    modules = []
    messages = []

    # Iterate over each line in the time tracking file
    for line in time_tracking_file.read_text().splitlines():
        timestamps.append(
            float(re.findall(r'(?<=\[)\d+\.\d+(?=\])', line)[0])
        )
        layers.append(
            int(re.findall(r'(?<=\]\s)\d+(?=\s\()', line)[0])
        )
        modules.append(
            re.findall(r'(?<=\().+(?=\))', line)[0]
        )
        messages.append(
            re.findall(r'(?<=\)\s).+', line)[0]
        )

    # Create and return pandas DataFrame
    return pd.DataFrame({
        'Layer': layers,
        'Module': modules,
        'Message': messages,
        'Timestamp': timestamps,
    })
