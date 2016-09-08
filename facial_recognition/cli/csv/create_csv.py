#!/usr/bin/env python

import click
import sys
import os.path


@click.argument('basepath')
@click.command()
def csv(basepath):
    """

    This command will create a CSV file from a face database with the following hierarchy:

    \b
    .
    |-- README
    |-- s1
    |   |-- 1.pgm
    |   |-- ...
    |   |-- 10.pgm
    |-- s2
    |   |-- 1.pgm
    |   |-- ...
    |   |-- 10.pgm
    ...
    |-- s40
    |   |-- 1.pgm
    |   |-- ...
    |   |-- 10.pgm
    """
    SEPARATOR = ";"
    label = 0
    for dirname, dirnames, filenames in os.walk(basepath):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                print "%s%s%d" % (abs_path, SEPARATOR, label)
            label = label + 1
