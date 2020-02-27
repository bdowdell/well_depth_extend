#!/usr/bin/env/ python

import os

def get_file_list(path=os.getcwd()):
    """This function returns the contents of a given directory
    Assumes path a string
    Defaults path to be current working directory
    Returns a list
    """
    return os.listdir(path)

