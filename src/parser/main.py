# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.parser.utils.dataframe import convert_to_dataframe
from src.parser.utils.merge import merge_dataframes
from pathlib import Path
import pandas as pd
import click

@click.group()
def cli():
    """ Image Processing Performance - Time Tracking Parser

        Author:
            Benedikt Schwering <bes9584@thi.de>
    """
    pass

@cli.command(
    name='parse',
    help='Parse time tracking data.'
)
@click.option(
    '--output',
    '-o',
    type=click.Path(
        resolve_path=True,
        dir_okay=False,
        file_okay=True,
    ),
    default='out.xlsx',
    show_default=True,
)
@click.argument(
    'time_tracking_files',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
    required=True,
    nargs=-1,
)
def parse(output: str, time_tracking_files: tuple[str, ...]):
    """ Parse time tracking files to Excel format.
    
        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            time_tracking_files (tuple[str, ...]): Time tracking files to parse.
    """
    with pd.ExcelWriter(output) as writer:
        # Iterate over time tracking files
        for time_tracking_file in time_tracking_files:
            # Convert to Path object
            time_tracking_file = Path(time_tracking_file)

            # Convert to DataFrame and write to Excel
            convert_to_dataframe(
                time_tracking_file=time_tracking_file,
            ).to_excel(
                writer,
                sheet_name=Path(time_tracking_file).name,
                index=False,
            )

@cli.command(
    'merge',
    help='Parse time tracking files and merge them.'
)
@click.option(
    '--output',
    '-o',
    type=click.Path(
        resolve_path=True,
        dir_okay=False,
        file_okay=True,
    ),
    default='out.xlsx',
    show_default=True,
)
@click.argument(
    'time_tracking_path',
    type=click.Path(
        exists=True,
        resolve_path=True,
        dir_okay=True,
        file_okay=False,
    ),
    required=True,
)
def merge(output: str, time_tracking_path: str):
    """ Parse time tracking files and merge them based on used algorithms.

        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            time_tracking_path (str): Path to time tracking files directory.
    """
    # Convert to Path object
    time_tracking_path = Path(time_tracking_path)
    
    # Initialize empty list
    dataframes: list[tuple[str, pd.DataFrame]] = []

    # Get all time tracking files in the given path and sort them
    time_tracking_files = list(time_tracking_path.glob('*.txt'))
    time_tracking_files.sort()

    # Iterate over each time tracking file in the given path and convert to DataFrame
    for time_tracking_file in time_tracking_files:
        dataframes.append(
            (
                time_tracking_file.name.replace('.txt', ''),
                convert_to_dataframe(
                    time_tracking_file=time_tracking_file,
                ),
            )
        )

    # Merge DataFrames based on time tracking events and write to Excel
    with pd.ExcelWriter(output) as writer:
        for key, df in merge_dataframes(
            dataframes=dataframes,
        ).items():
            df.to_excel(
                writer,
                sheet_name=key,
                index=False,
            )
