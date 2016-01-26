#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2016 Sebastien Quioc

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
import json
import sys

def group_from_iterable(iterable, pivots):
    """
    Group items from the iterable with a pivot

    >>> group_from_iterable([{'people': 'Alice', 'value':'7'}, {'people': 'Josh', 'value':'6'}, {'people': 'Alice', 'value': '10'}], ["people"])
    {'Josh': [{'value': '6', 'people': 'Josh'}], 'Alice': [{'value': '7', 'people': 'Alice'}, {'value': '10', 'people': 'Alice'}]}
    """
    group = {}
    for item in iterable:
        pivot_value = '\t'.join(map(lambda pivot_name: item[pivot_name], pivots))
        group[pivot_value] = group.get(pivot_value, []) + [item]
    return group

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="group input entries according to a list of pivot")
    parser.add_argument('pivot', metavar="P", nargs='+', help='a pivot')
    parser.add_argument('--test', dest='test', action='store_true', help="test the group function")
    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
    else:
        for pivot, group in group_from_iterable(map(json.loads, sys.stdin.readlines()), args.pivot).items():
            print json.dumps({pivot: group})

