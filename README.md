data_tools
============

A Set of command line tools to manipulate data or to do some statistics

Installing from github `pip install -e git://github.com/squioc/data_tools`

Installing from source `python setup.py install`

Most of this tools accept only one-column lines.

## Usage

### max.py

Compute the max value of input lines

Example:

    $ cat sample | cut -f12 | max.py
    100.0

### min.py

Compute the min value of input lines

Example:

    $ cat sample | cut -f12 | min.py
    -5.0

### avg.py

Compute the average value of input lines

Example:

    $ cat sample | cut -f12 | avg.py
    29.5

### sum.py

Compute the sum of input lines

Example:

    $ cat sample | cut -f12 | sum.py
    130.0

### substring.py

Substring input lines

Example:

    $ echo averylongstring | substring.py 9 6
    string

