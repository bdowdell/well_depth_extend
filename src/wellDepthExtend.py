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

def dog_leg_severity(md, inc, az):
    """Assumes md, inc, and az are pandas series or numpy 1d array
    Calculates Dog Leg Severity
    Returns a numpy 1d array
    """
    # initialize an empty numpy array for Dog Leg Severity
    dls = np.zeros(len(md))
    # hard code the dog leg severity to be zero at the first sample
    dls[0]= 0
    # calculate measured depth increment, skipping the first sample
    mdStep = np.diff(md[1:], n=1)
    # create inc1, inc2 arrays offset by 1 index
    inc1 = np.deg2rad(inc[0:-1])
    inc2 = np.deg2rad(inc[1:])
    # create az1, az2 arrays offset by 1 index
    az1 = np.deg2rad(az[0:-1])
    az2 = np.deg2rad(az[1:])
    # compute dog leg severity
    dls[1:] = (np.rad2deg(np.arccos((np.cos(inc1) * np.cos(inc2))
    + (np.sin(inc1) * np.sin(inc2)) * np.cos(az2 - az1))) * (30 / mdStep))
    return dls

def minimum_curvature():
    """This function corrects wellbore deviation using the minimum curvature method
    Returns a numpy 1d array
    """
    pass

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

