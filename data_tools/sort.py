#! /usr/bin/python

import argparse
import sys

def sort_from_iterable(iterable):
    """
    Return a sorted iterable

    >>> sort_from_iterable([1, -2, 35, 11, 28])
    [-2, 1, 11, 28, 35]
    """
    l = list(iterable)
    l.sort()
    return l

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sort input entries")
    parser.add_argument('--test', dest='test', action='store_true')
    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
    else:
        map(lambda x: sys.stdout.write(str(x) + "\n"), sort_from_iterable(map(float, sys.stdin.readlines())))

