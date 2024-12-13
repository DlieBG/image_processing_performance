# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.parser.utils.dataframe import convert_to_dataframe, merge_all
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
@click.argument(
    'time_tracking_files',
    type=click.Path(
        exists=True,
        resolve_path=True,
    ),
    required=True,
    nargs=-1,
)
def parse(time_tracking_files: tuple[str, ...]):
    """ Parse time tracking files to csv format.
    
        Author:
            Benedikt Schwering <bes9584@thi.de>

        Args:
            time_tracking_files (tuple[str, ...]): Time tracking files to parse.
    """
    with pd.ExcelWriter('out.xlsx') as writer:
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
