#!/usr/bin/env python
# -*- coding: UTF8 -*-

from distutils.core import setup


version = "0.1.0"
setup(name='data_tools',
        version=version,
        description='Command line tools for data manipulation',
        author='Sebastien Quioc',
        author_email='sebastien.quioc@yahoo.com',
        url='https://github.com/squioc/data_tools',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python',
            'Intended Audience :: System Administrators',
            'Topic :: Terminals',
        ],
        download_url="https://github.com/squioc/data_hacks/archive/v%s.zip" % version,
        scripts = [
            "data_tools/avg.py",
            "data_tools/min.py",
            "data_tools/max.py",
            "data_tools/sum.py",
            "data_tools/substring.py",
        ]
    )
