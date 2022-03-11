#!/usr/bin/env python3.10

import json
from pygments import highlight, lexers, formatters

def pprint(obj, name=None):
    json_str = json.dumps(obj, indent='\t')
    string_fmt = highlight(
            json_str,
            lexers.JsonLexer(),
            formatters.TerminalFormatter()
        )
    if name:
        string_fmt = name + "=" + string_fmt
    print(string_fmt, end=None)


