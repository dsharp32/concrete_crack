#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

The aim of this file is to apply the functions 
find_threshold() and find_concrete_crack_bool()
that you have written for Assignment 2 to a real-life image.

"""

# %% import 
import find_threshold as thres # Function to be tested 
import find_concrete_crack_bool as find_crack # Function to be tested 
import find_crack_area as find_area
import numpy as np
import matplotlib.pyplot as plt # for showing images


# %% 
# Constants to convert colour images (Red, green, blue colour scale)
# to greyscale
RGB_to_greyscale = [0.2126,0.7152,0.0722] # Convert red-green-blue 


# %% Load the image from the file oncrete_crack1.jpg
# Coloured image in 3-d numpy array
concrete_image_rbg = plt.imread('concrete_crack1.jpg') 

# Convert to greyscale
concrete_image = np.sum(concrete_image_rbg * RGB_to_greyscale, axis = 2)  
 
# %% Call find_threshold() from Assignment 2 and then 
# call find_concrete_crack_bool()

# The num_points parameter for find_threshold()
num_points = 16

# Call find_threshold() to determine the threshold
your_threshold = thres.find_threshold(concrete_image, num_points)

# Call find_concrete_crack_bool() to find the crack  
concrete_crack_bool = find_crack.find_concrete_crack_bool(concrete_image,your_threshold)

crack_area = find_area.find_crack_area(concrete_crack_bool)

# %% 
# The expected answer
expected_answer = 192.333

# Compare your answer to expected answer
TOL = 1e-1    

# Compare your_answer against the expected_answer
if abs(your_threshold - expected_answer) < TOL:
    print('The crack area is',crack_area)
    print('Your answer is correct')
else:
    print('Your answer is NOT correct')
    print('The expected answer is', expected_answer)
    print('Your answer is',your_threshold)
              
# %% Plot the image
plt.figure()
plt.imshow(concrete_image, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('The given concrete image')
plt.show()

plt.figure()
plt.imshow(concrete_crack_bool, cmap = 'gray', vmin = 0, vmax = 1)
plt.title('The Boolean image created by your calculated threshold')
plt.show()
                 