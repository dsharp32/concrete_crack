#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Final File for find_concrete_crack_bool()

@author: Daniel Sharp
"""

def find_concrete_crack_bool(concrete_image, threshold):
    """
    Creates boolean array from numerical array.

    Parameters
    ----------
    concrete_image : TYPE NNumpy array
        DESCRIPTION. Array of values from 0 - 255 representing image
    threshold : TYPE float
        DESCRIPTION. Threshold to determine if Boolean value is 'True' or 'False'.

    Returns
    -------
    concrete_crack_bool : TYPE Boolean Array
        DESCRIPTION. Boolean representation of image.

    """   
    # Creates boolean array where all elements less than threshold are 'True'.     
    concrete_crack_bool = concrete_image < threshold
    
    return concrete_crack_bool 
