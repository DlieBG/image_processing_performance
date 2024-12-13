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
    indices = []
    timestamps = []
    layers = []
    modules = []
    messages = []

    # Iterate over each line in the time tracking file
    for i, line in enumerate(time_tracking_file.read_text().splitlines()):
        indices.append(i)
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
        'Index': indices,
        'Layer': layers,
        'Module': modules,
        'Message': messages,
        'Timestamp': timestamps,
    })
    
def merge_all(dataframes: list[pd.DataFrame]) -> pd.DataFrame:
    dataframe = dataframes[0]
    dataframe = dataframe[dataframe['Layer'] == 0]

    for i, df in enumerate(dataframes[1:]):
        df = df[df['Layer'] == 0]
        dataframe = pd.merge(
            dataframe,
            df[['Layer', 'Module', 'Message', 'Timestamp']],
            on=['Layer', 'Module', 'Message'],
            how='left',
            suffixes=('', f'_{i}'),
        )

    return dataframe.sort_values(by=['Timestamp'])
