#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Final File for find_crack_area()

@author: Daniel Sharp 
"""

import numpy as np 

def find_crack_area(concrete_crack_bool):
    """
    Computes total area of crack.

    Parameters
    ----------
    concrete_crack_bool : TYPE Boolean array
        DESCRIPTION. Boolean representation of image.

    Returns
    -------
    crack_area : TYPE int
        DESCRIPTION. Number of elements defined as the crack.

    """
    # Count and returns number of 'True' elements in array.
    crack_area = np.sum(concrete_crack_bool == True) 
    
    return crack_area  