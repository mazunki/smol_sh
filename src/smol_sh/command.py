#!/usr/bin/env python3.10

import re
from smol_sh.utils import pprint

class Command:
    """
        A class where commands are created. After instantiation, it can be recalled
        through the usage of self.spawn().

        Beware: The order of options (aka --some "value", -s "value") will be preserved
        only in itself, and not to the command.

        Short options will be passed before long options. Arguments will be passed in last.
    """
    def __init__(self, prog, *args, **kwargs):
        self.prog = prog
        self.args_ = args
        self.kwargs_ = kwargs
        self.short_opts = {}
        self.long_opts = {}

        for key, value in self.kwargs_.items():
            print(f"{key=}, {value}=")
            if len(key) == 1:
                self.short_opts[key] = value
            else:
                self.long_opts[key] = value

        pprint(f"{self.short_opts=}")
        pprint(f"{self.long_opts=}")

    @classmethod
    def parse_str(cls, cmd_string):
        def to_dict_value(key, value, qvalue):
            print(f"{key=}, {value=}, {qvalue=}")
            if value == None and qvalue == None:
                return key, True
            elif value or qvalue:
                return key, (value or qvalue)
            elif value is not None:
                return key, value
            elif qvalue is not None:
                return key, qvalue

        short = {}
        long = {}
        print(cmd_string, end="\n\n")

        quoted_word = "'(?P<qvalue>[^']*)'"
        unquoted_word = "(?P<value>\w+)"

        command_reg = re.compile("^(?:" + "|".join([quoted_word, unquoted_word]) + ")")

        long_key = "--(?P<key>\w+)"
        long_reg = re.compile("(?<=\s)" + long_key + "=(?:" + "|".join([quoted_word, unquoted_word]) + ")")

        short_key = "-(?P<key>\w+)"
        short_reg = re.compile("(?<=\s)" + short_key + "(?:" + quoted_word + "|=?" + unquoted_word + ")?")

        base_ = [ x.group("qvalue", "value") for x in command_reg.finditer(cmd_string) ][0]
        long_ = [ x.group("key", "qvalue", "value") for x in long_reg.finditer(cmd_string) ]
        short_ = [ x.group("key", "qvalue", "value") for x in short_reg.finditer(cmd_string) ]

        base = base_[0] or base_[1]
        long = dict(to_dict_value(*kqv) for kqv in long_)
        short = dict(to_dict_value(*kqv) for kqv in short_)

        print(short)
        pprint(base, "base")
        pprint(short, "short")
        pprint(long, "long")
        print("\n")
        return (base, short, long)

    def __str__(self):
        return " ".join((
            self.prog,
            *(f"--{kw} {val}" for kw, val in self.kwargs.items()),
            *self.args,
        ))
        

    def spawn(self):
        os.Popen(self.program_path, *self.program_args)


