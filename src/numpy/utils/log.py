# -*- coding: utf-8 -*-
"""
Image Processing Performance Python
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from datetime import datetime
from rich import print
import inspect

reference = datetime.now()

def log(message: str):
    global reference
    elapsed = datetime.now() - reference

    print(
        f'[blue][{elapsed.total_seconds()}][/]',
        f'[red]{len(inspect.stack()) - 9}[/]',
        f'[green]({inspect.stack()[1].function})[/]',
        message,
    )
