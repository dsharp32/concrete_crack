#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Final File for classify_all_pixels()

@author:Daniel Sharp
"""
# import 
import numpy as np
import classify_a_pixel as classify_1

def classify_all_pixels(concrete_crack_bool):
    """
    Classifys all elements in input boolean array as either 0,1 or 2.
    Calls classify_a_pixel function.
    
    Parameters
    ----------
    concrete_crack_bool : TYPE Boolean Array
        DESCRIPTION. Boolean representation of image

    Returns
    -------
    classified_array : TYPE Array
        DESCRIPTION. Numpy array with elements 0,1 or 2.

    """
    c = concrete_crack_bool
    
    # Get all indices of concrete_crack_bool as a list.
    indices_list = [] 
    for index, x in np.ndenumerate(c):
            indices_list.append(index)
    
    # Iterate over indices list and classify each pixel with classify_1 module.
    classified_list = [] 
    for i,j in indices_list:
        classified_list.append(classify_1.classify_a_pixel(c,i,j))
    
    # Convert classfied list to array
    classified_array = np.array(classified_list) 
    
    # Reshape array to same shape as input array.
    classified_array = np.reshape(classified_array,c.shape) 

    return classified_array