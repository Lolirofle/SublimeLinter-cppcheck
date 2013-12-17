#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Edwin P
# Copyright (c) 2013 Edwin P
#
# License: MIT
#

"""This module exports the Cppcheck plugin class."""

from SublimeLinter.lint import Linter, util


class Cppcheck(Linter):

    """Provides an interface to cppcheck."""

    syntax = ('c', 'c++', 'c improved')
    cmd = 'cppcheck --enable=style --enable=warning --quiet'
    executable = 'cppcheck'
    regex = (
        r'^\[.+?:(?P<line>\d+)\]: '
        r'\((?:(?P<error>error)|(?P<warning>(warning|style|performance|portability)))\)'
        r'(?P<message>.+)'
    )
    tempfile_suffix = ' '
    line_col_base = (1, 1)
    error_stream = util.STREAM_STDERR
