
import os
import re

from smol_sh import utils
from smol_sh.command import Command

class SmolShell:
    def __init__(self):
        self.env = os.environ
        self.cmd = Command.parse_str("'test' abc def --she='did ballet' -I --skater=boy punk -v=a -V")
        self.cmd = Command.parse_str("test abc def --she='did ballet' -I --skater=boy punk -v=a -V")
        self.cmd = Command.parse_str("'test cmd' abc def --she='did ballet' -d'' -I --skater=boy punk -v=a -V")
        # print(self.cmd)

    def refresh_environment(self):
        for k, v in os.environ.items():
            exec(f"self.{k}={repr(v)}")
    
    def print_env(self):
        for k, v in self.env.items():
            print(f"{k} = '{repr(v)}'")

