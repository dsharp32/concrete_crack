#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Final File for classify_a_pixel()

@author: Daniel Sharp
"""

def classify_a_pixel(concrete_crack_bool,i,j):
    """
    Identifies input element's position in array from index value.
    Element can be a corner (NW, SW, NE, SE), an edge (N,S,E,W) or interior.
    Elements N,S,E,W neighbours bool value is identified and used to classify element.
    
    Parameters
    ----------
    concrete_crack_bool : TYPE Numpy Array
        DESCRIPTION. Bopolean array representing greyscale image.
    i : TYPE int
        DESCRIPTION. i co-ordinate of array.
    j : TYPE int
        DESCRIPTION. j co-ordinate of array.

    Returns
    -------
    pixel_type : TYPE int
        DESCRIPTION. 0 for 'False' array values.
                     1 for 'True' values at least one N,S,E,W neighbour as False.
                     2 for 'True' values with all N,S,E,W neighbours as 'True.'
    """
    c = concrete_crack_bool 
    pixel = c[i,j]
    
    length_i = c.shape[0]-1
    length_j = c.shape[1]-1
    
    # if pixel is in crack 
    if pixel == True:
        # if pixel is in north west corner
        if (i == 0 and j == 0): 
            if (c[i+1,j] and c[i,j+1]) == True: 
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is in south west corner
        elif (i == length_i and j == 0):
            if (c[i-1,j] and c[i,j+1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is in north east corner        
        elif (i == 0 and j == length_j):
            if (c[i+1,j] and c[i,j-1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is in south east corner         
        elif (i == length_i and j == length_j):
            if (c[i-1,j] and c[i,j-1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is on north edge and not a corner        
        elif (i == 0 and (j != 0 or length_j)):
            if (c[i+1,j] and c[i,j+1] and c[i,j-1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is on south edge and not a corner    
        elif (i == length_i and (j != 0 or length_j)):
            if (c[i-1,j] and c[i,j+1] and c[i,j-1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
        
        # if pixel is on west edge and not a corner
        elif (j == 0 and (i != 0 or length_i)):
            if (c[i-1,j] and c[i+1,j] and c[i,j+1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
                
        # if pixel is on east edge and not a corner    
        elif (j == length_j and (i != 0 or length_i)):
            if (c[i-1,j] and c[i+1,j] and c[i,j-1]) == True:
                pixel_type = 2
            else:
                pixel_type = 1
                
        # classify all other 'True' pixel types not on corner or edge.
        else:
            if (c[i-1,j] and c[i+1,j] and c[i,j+1] and c[i,j-1]) == True:
                pixel_type = 2
            else:
               pixel_type = 1
    
    # Classify all 'False' pixel as 0
    else:
        pixel_type = 0
        
    return pixel_type





    