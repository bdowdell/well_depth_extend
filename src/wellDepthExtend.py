#!/usr/bin/env/ python

import os

def get_file_list(path):
    """This function returns the contents of a given directory
    Assumes path a string
    Returns a list
    """
    return os.listdir(path)

