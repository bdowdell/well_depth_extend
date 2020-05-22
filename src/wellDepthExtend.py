#!/usr/bin/env/ python

import os
import pandas as pd
import numpy as np
from bisect import bisect_left

def get_file_list(path=os.getcwd()):
    """
    Gets a listing of well files in a specified directory

    Parameters:

    path (string): The directory path for the well files

    Returns:

    list: list of files in specified directory
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

def dog_leg_severity(md, inc, az, units):
    """Calculates the dog leg severity as input to minimum curvature for TVD correction

    Parameters:

    md (ndarray-like): Measured Depth

    inc (ndarray-like): Wellbore inclination

    az (ndarray-like): Wellbore azimuth
    
    units (string): Depth measurement units, 'm' or 'ft'

    Returns:

    ndarray, ndarray: Dog Leg, Dog Leg Severity
    """
    # initialize an empty numpy array for Dog Leg Severity
    dls = np.zeros(len(md))
    dl = np.zeros(len(md))
    # hard code the dog leg severity to be zero at the first sample
    dl[0] = 0
    dls[0]= 0
    # calculate measured depth increment, skipping the first sample
    mdStep = np.diff(md, n=1)
    # create inc1, inc2 arrays offset by 1 index
    inc1 = np.deg2rad(inc[0:-1])
    inc2 = np.deg2rad(inc[1:])
    inc2.reset_index(drop=True, inplace=True)
    # create az1, az2 arrays offset by 1 index
    az1 = np.deg2rad(az[0:-1])
    az2 = np.deg2rad(az[1:])
    az2.reset_index(drop=True, inplace=True)
    a = np.multiply(np.sin(inc1), np.sin(inc2))
    b = np.cos(az2 - az1)
    c = np.multiply(a, b)
    d = np.multiply(np.cos(inc1), np.cos(inc2))
    e = np.arccos(c + d)
    dl[1:] = np.rad2deg(e)
    try:
        if units.lower() == 'm':
            f = np.multiply(dl, 30.)
        elif units.lower() == 'ft':
            f = np.multiply(dl, 100.)
        else:
            raise ValueError
    except ValueError:
        raise ValueError('Invalid units')
    g = np.divide(f[1:], mdStep)
    dls[1:] = g
    return dl, dls

def minimum_curvature(md, inc, dl, tvd0):
    """This function corrects wellbore deviation using the minimum curvature method
    
    Parameters:

    md (ndarray-like): Measured Depth

    inc (ndarray-like): Wellbore Inclination

    dl (ndarray-like): Dog Leg
    
    tvd0 (float): True Vertical Depth of initial depth sample (usually 0.0)

    Returns:

    ndarry: True Vertical Depth
    """
    # initialize an empty numpy array for TVD
    tvd = np.zeros(len(md))
    # hard code the TVD of the first sample to be zero
    tvd[0] = tvd0
    # create md1, md2 arrays offset by 1 index
    md1 = md[0:-1]
    md2 = md[1:]
    md2.reset_index(drop=True, inplace=True)
    # create inc1, inc2 arrays offset by 1 index
    inc1 = np.deg2rad(inc[0:-1])
    inc2 = np.deg2rad(inc[1:])
    inc2.reset_index(drop=True, inplace=True)
    # calculate ratio factor
    rF = np.zeros(len(md))
    a_rF = np.tan(np.divide(np.deg2rad(dl), 2.))
    b_rF = np.zeros(len(a_rF))
    b_rF[dl > 0] = np.divide(2., np.deg2rad(dl[dl > 0]))
    b_rF[dl == 0] = 1
    rF = np.multiply(a_rF, b_rF)
    # calculate TVD
    a = np.cos(inc1) + np.cos(inc2)
    b = np.divide((md2 - md1), 2.)
    c = np.multiply(rF[1:], b)
    d = np.multiply(a, c)
    tvd[1:] = np.cumsum(d) + tvd0
    return tvd

def getClosestValues(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

def uniform_md(start_depth=0, kb=32, stop_depth=10000, inc=0.5, units='ft'):
    """This function builds uniformly spaced depth reference curves
    Defaults start_depth, kb, stop_depth, inc, and units
    Returns a pandas series
    """
    # calcuate how many samples are needed for max TD
    size = int(round(stop_depth, 1)) + 1
    md = list()
    for i in range(0, size * 10000, int(inc * 10000)):
        md.append(float(i) / 10000)
    
    # create a dataframe for the uniform md
    return pd.DataFrame({'MD':md})


def reindex_curves(original_curves, reference_curves):
    """This function merges the original curves with the reference curves
    Assumes original_curves, reference_curves a pandas dataframe
    Returns a pandas dataframe
    """
    pass

