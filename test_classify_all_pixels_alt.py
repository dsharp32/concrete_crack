#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

You can use this file to test your classify_all_pixels().

This file containing 5 test cases which you can choose by
adjusting the variable test_num in Line 21. 

You can use this file to come out with additional tests. 
"""

# %% import 
import classify_all_pixels as classify_all # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image
from matplotlib.colors import ListedColormap # For plotting 

# %% Tests 
test_num = 0 # test_num can be 0, 1, 2, 3, 4

if test_num == 0:
    # The binarised concrete image   
    concrete_crack_bool = np.array(
      [[ True,  True, False, False, False],
       [ True,  True,  True, False, False],
       [False,  True,  True,  True, False],
       [False, False,  True, False, False],
       [False, False,  True, False, False],
       [False,  True,  True,  True, False]])
    
    expected_answer = np.array(
      [[2, 1, 0, 0, 0],
       [1, 2, 1, 0, 0],
       [0, 1, 2, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 2, 1, 0]])
    
elif 1 <= test_num <= 4: 
    # Load the concrete image and expected answer from the ref file 
    ref_data = np.load('ref_data_' + str(test_num) + '.npz', allow_pickle = True)
    concrete_crack_bool = ref_data['concrete_crack_bool']
    expected_answer = ref_data['image_pixel_status']
         
else: 
    print('Not a valid test number')


# %% Run the function and check the answers

# Call the function classify_all_pixels() and store the answer in your_answer
your_answer = classify_all.classify_all_pixels(concrete_crack_bool)

# Do some basic checks before making a comparison 
# These basic checks are: Is it a numpy array? Is dtype bool?
#                         Does it have the correct shape?
# If all these types are correct, then compare the entries 
if type(your_answer) is np.ndarray:
    # your answer is a numpy array
    if 'int' in your_answer.dtype.name:
        # your_answer is a numpy array of bool dtype
        if your_answer.shape == expected_answer.shape:
            # your_answer has the right type and shape
            if np.all(your_answer == expected_answer):
                # All entries are correct
                print('Your answer is correct')
            else: 
                # Not all entries are correct 
                print('Some elements in your answers are incorrect')
                
            # Plot the given Boolean image
            plt.figure()
            plt.imshow(concrete_crack_bool, cmap = 'gray', vmin = 0, vmax = 1)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = concrete_crack_bool.shape[1]-0.5
            y_min = -0.5
            y_max = concrete_crack_bool.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar()
            plt.title('The given Boolean image')
            plt.show()
            
            # Plot your answer
            plt.figure()
            cmap_black_cyan_blue = ListedColormap(['black','cyan','blue'])
            plt.imshow(your_answer, cmap = cmap_black_cyan_blue, vmin = 0, vmax = 2)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = your_answer.shape[1]-0.5
            y_min = -0.5
            y_max = your_answer.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar(ticks=[0,1,2])
            plt.clim(-0.5, 2.5)
            plt.title('Your answer: Black (Type 0), Cyan (Type 1), Blue (Type 2)')
            plt.show()
            
            # Plot the expected answer
            plt.figure()
            plt.imshow(expected_answer, cmap = cmap_black_cyan_blue, vmin = 0, vmax = 2)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = expected_answer.shape[1]-0.5
            y_min = -0.5
            y_max = expected_answer.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar(ticks=[0,1,2])
            plt.clim(-0.5, 2.5)
            plt.title('Expected answer: Black (Type 0), Cyan (Type 1), Blue (Type 2)')            
            plt.show()
        else:
            print('Your answer has a shape of:',your_answer.shape)
            print('The expecte answer has a shape of:',expected_answer.shape)
    else:
        print('Your function output did not return a numpy array of int type')  
else:
    print('Your function output did not return a numpy array')    
