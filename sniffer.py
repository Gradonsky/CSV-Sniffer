#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*******************
CSV Dialect Sniffer
*******************

This module goes through the common
delimiters and thereby tries to acknowledge the
CSV File's dialect
"""
__author__ = "Gradonski Janusz"
__license__ = "GPL"
__version__ = "1.0"

import csv
import sys



POSSIBLE_DELIMITERS = [',', '\t', ';', ' ', ':', '|']

def sniff_dialect(input):
    """
    A functional version of ``csv.Sniffer().sniff``, that extends the
    list of possible delimiters to include some seen in the wild.
    """
    try:
        dialect = csv.Sniffer().sniff(input, POSSIBLE_DELIMITERS)
    except:
        dialect = None

    return dialect
