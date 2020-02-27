#!/usr/bin/env/ python

import os
import pandas as pd
import numpy as np

def get_file_list(path=os.getcwd()):
    """This function returns the contents of a given directory
    Assumes path a string
    Defaults path to be current working directory
    Returns a list
    """
    return os.listdir(path)

def pair_well_files(file_list):
    """This function reads in the contents of a directory
    And pairs unique well LAS file with well deviation survey
    Assumes file_list a list
    Returns a dictionary
    """
    pass

def read_well_las(well_file):
    """This function reads in a LAS file
    Assumes well_file a string
    Returns a pandas dataframe
    """
    pass

def read_dev_surv(dev_surv_file):
    """This function reads in a CSV file
    Assumes dev_surv_file a string
    Returns a pandas dataframe
    """
    pass

def reference_curves(dev_surv, start_depth=0, kb=32, stop_depth=10000, inc=5, units='ft'):
    """This function builds uniformly spaced depth reference curves
    Defaults start_depth, kb, stop_depth, inc, and units
    Assumes dev_surv a pandas dataframe
    Returns a pandas dataframe
    """
    pass

