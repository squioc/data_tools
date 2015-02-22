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

import argparse
import sys

def avg_from_iterable(iterable):
    """
    Return the average from the iterable

    >>> avg_from_iterable([1, -2, 35, 11, 28])
    14.4
    """
    sum, length = reduce(lambda acc, item: (acc[0] + item[1], item[0] + 1), enumerate(iterable))
    return float(sum)/length

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="compute the average of input entries")
    parser.add_argument('--test', dest='test', action='store_true', help="execute unit doctests")
    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
    else:
        print avg_from_iterable(map(float, sys.stdin.readlines()))

