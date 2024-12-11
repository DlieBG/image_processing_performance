# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from rich import print
import inspect, time

def log(message: str):
    print(
        f'[blue][{time.process_time()}][/]',
        f'[red]{len(inspect.stack()) - 9}[/]',
        f'[green]({inspect.stack()[1].function})[/]',
        message,
    )
    
