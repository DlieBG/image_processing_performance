# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from rich import print
import time

def log(component: str, layer: int, message: str):
    print(
        f'[blue][{time.process_time()}][/]',
        f'[red]{layer}[/]',
        f'[green]({component})[/]',
        message,
    )
    
