#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2015 Sebastien Quioc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import print_function
import sys
import argparse
import functools

def substring(entry, start, length):
    """
    >>> substring(None, 12, 6)
    ''
    >>> substring("tooshort", 12, 6)
    ''
    >>> substring("thisverylongstringshouldbetruncated", 12, 6)
    'string'
    >>> substring("thisstringshouldnotbetruncated", 0, 30)
    'thisstringshouldnotbetruncated'
    """
    if entry is None or len(entry) < start:
        return ""
    elif len(entry) < start + length:
        return entry[start:]
    else:
        return entry[start:start+length]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='substring input lines')
    parser.add_argument('--test', dest='test', action='store_true', help="execute unit doctests")
    parser.add_argument('start', nargs='?', default=0, type=int, help='the start of the substring')
    parser.add_argument('length', nargs='?', type=int, help='the length of the substring')
    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
    else:
        currified = functools.partial(substring, start=args.start, length=args.length)
        map(print, map(currified, sys.stdin.readlines()))

