# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
import pandas as pd

def merge_dataframes(dataframes: list[tuple[str, pd.DataFrame]]) -> dict[pd.DataFrame]:
    """ Merge DataFrames based on time tracking events.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            dataframes (list[tuple[str, pd.DataFrame]]): DataFrames with original filenames to merge.

        Returns:
            dict[pd.DataFrame]: Merged DataFrames.
    """
    # Filter out the first layer
    dataframes = [
        (
            df[0],
            df[1][df[1]['Layer'] == 0],
        )
            for df in dataframes
    ]

    # Group DataFrames by the used algorithm (second message - "finish <algorithm name>")
    grouped_dfs = {}
    for df in dataframes:
        key = df[1]['Message'].iloc[1].replace('finish ', '')
        if key not in grouped_dfs:
            grouped_dfs[key] = []

        grouped_dfs[key].append(df)

    # Merge DataFrames based on the event messages and rename timestamps to original filenames
    merged_dfs = {}
    for key, dfs in grouped_dfs.items():
        # Copy the first DataFrame and rename the timestamp column
        merged_df = dfs[0][1].copy()
        merged_df.rename(columns={'Timestamp': dfs[0][0]}, inplace=True)

        # Merge the remaining DataFrames and rename the timestamp columns
        for df in dfs[1:]:
            # Only keep the relevant columns message and timestamp
            temp_df = df[1][['Message', 'Timestamp']].copy()
            temp_df.rename(columns={'Timestamp': df[0]}, inplace=True)

            # Merge the DataFrames based on the message column
            merged_df = merged_df.merge(
                temp_df,
                on='Message',
                how='left',                
            )

        merged_dfs[key] = merged_df
    
    return merged_dfs
