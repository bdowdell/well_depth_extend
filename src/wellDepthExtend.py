#!/usr/bin/env/ python

import os
import pandas as pd
import numpy as np

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

def dog_leg_severity(md, inc, az):
    """Calculates the dog leg severity as input to minimum curvature for TVD correction

    Parameters:

    md (ndarray-like): Measured Depth

    inc (ndarray-like): Wellbore inclination

    az (ndarray-like): Wellbore azimuth

    Returns:

    ndarray: Dog Leg Severity
    """
    # initialize an empty numpy array for Dog Leg Severity
    dls = np.zeros(len(md))
    # hard code the dog leg severity to be zero at the first sample
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
    # compute dog leg severity
    a = np.multiply(np.cos(inc1), np.cos(inc2))
    b = np.multiply(np.sin(inc1), np.sin(inc2))
    c = np.multiply(b, np.cos(az2 - az1))
    d = np.rad2deg(np.arccos(a + c))
    e = np.multiply(d, np.divide(30., mdStep))
    dls[1:] = e
    return dls

def minimum_curvature(md, inc, dls):
    """This function corrects wellbore deviation using the minimum curvature method
    
    Parameters:

    md (ndarray-like): Measured Depth

    inc (ndarray-like): Wellbore Inclination

    dls (ndarray-like): Dog Leg Severity

    Returns:

    ndarry: True Vertical Depth
    """
    # initialize an empty numpy array for TVD
    tvd = np.zeros(len(md))
    # hard code the TVD of the first sample to be zero
    tvd[0] = 0.0
    # create md1, md2 arrays offset by 1 index
    md1 = md[0:-1]
    md2 = md[1:]
    md2.reset_index(drop=True, inplace=True)
    # create inc1, inc2 arrays offset by 1 index
    inc1 = np.deg2rad(inc[0:-1])
    inc2 = np.deg2rad(inc[1:])
    inc2.reset_index(drop=True, inplace=True)
    # calculate dog leg severity
    dogLegSev = np.deg2rad(np.divide(dls[1:], np.divide(30., (md2 - md1))))
    # note: we are dividing out a factor multiplied in dog_leg_severity
    # calculate curvature factor
    cF = np.zeros(len(md[1:]))
    cF[dogLegSev > 0] = np.divide(2., np.multiply(dogLegSev, np.tan(np.divide(dogLegSev, 2.))))
    cF[dogLegSev <= 0] = 1
    # calculate TVD
    a = md2 - md1
    b = np.cos(inc2) + np.cos(inc1)
    c = np.multiply(a, b)
    d = np.divide(c, 2.)
    e = np.multiply(d, cF)
    tvd[1:] = np.cumsum(e)
    return tvd

def reference_curves(dev_surv, start_depth=0, kb=32, stop_depth=10000, inc=0.5, units='m'):
    """This function builds uniformly spaced depth reference curves
    Assumes dev_surv a pandas dataframe
    Defaults start_depth, kb, stop_depth, inc, and units
    Returns a pandas series
    """
    pass

def reindex_curves(original_curves, reference_curves):
    """This function merges the original curves with the reference curves
    Assumes original_curves, reference_curves a pandas dataframe
    Returns a pandas dataframe
    """
    pass

