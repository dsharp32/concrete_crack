#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Final File for find_threshold()

@author: Daniel Sharp
"""

# import
import numpy as np
from operator import itemgetter

def find_threshold(concrete_image, num_points = 20):
    """
    Computes list of all potential thresholds.
    Computes cost of each threshold.
    Returns threshold with lowest cost.
    
    Parameters
    ----------
    concrete_image : TYPE Numpy array 
        DESCRIPTION. Elements 0 - 255 representing a greyscale image.
    num_points : TYPE, optional
        DESCRIPTION. The default is 20.

    Returns
    -------
    best_threshold : TYPE float
        DESCRIPTION. The threshold for determining the boolean values of the numerical array.

    """

    max_value = np.max(concrete_image) # Find maximum value in concrete image.
    min_value = np.min(concrete_image) # Find minimum value in concrete image.
    
    # Create array of evenly spaced floats between minimum value and maximum value in image array.
    pot_thresholds_array = np.linspace(min_value, max_value, num_points, endpoint = True)
    
    # Array of means of the potential thresholds and the minimum value in concrete_image.
    c_0_array = (pot_thresholds_array + min_value)/2
    
    # Array of means of the potential thresholds and the minimum value in concrete_image.
    c_1_array = (pot_thresholds_array + max_value)/2   
    
    # Create index list for potential thresholds array.
    pot_thresholds_index = list(range(num_points))
    
    cost_list = []
    
    # Iterate through potential thresholds list.
    for i in pot_thresholds_index:
        
        # Create an array of values less than and greater than for each threshold.
        less_than_array = concrete_image[concrete_image < pot_thresholds_array[i]]
        greater_than_array = concrete_image[concrete_image >= pot_thresholds_array[i]]
        
        # Subtract c_0_array value and square the result for all elements.
        cost_p0 = np.sum((less_than_array-c_0_array[i])**2)
        
        # Subtract c_1_array value and square the result for all elements.
        cost_p1 = np.sum((greater_than_array-c_1_array[i])**2)
        
        # Create list of total costs for each threshold. 
        total_cost = cost_p0 + cost_p1
        cost_list.append(total_cost)
    
    # Get index of minimum value in list of threshold costs.
    min_cost_index = min(enumerate(cost_list), key=itemgetter(1))[0]
    
    # Get corrosponding element from potential thresholds array.
    best_threshold = pot_thresholds_array[min_cost_index]
    
    return best_threshold

   



        


 

    
    