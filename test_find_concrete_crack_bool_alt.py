#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (20T1) 

You can use this file to test your find_concrete_crack_bool().

This file containing 5 test cases which you can choose by
adjusting the variable test_num in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_concrete_crack_bool as find_crack # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_num = 0 # test_num can be 0, 1, 2, 3, 4

# The thresholds for the tests 
threshold_list = [120, 205.7, 174, 188.4, 158.0]


if test_num == 0:
    # The concrete image 
    concrete_image = np.array(
      [[ 70, 106, 200, 216, 226],
       [ 33,  25,  38, 160, 225],
       [196,  99,  34,  29, 189],
       [218, 222,  22, 224, 221],
       [211, 192,  27, 186, 168],
       [191,  15,  28,  20, 199]])
    
    threshold = threshold_list[test_num]
        
    expected_answer = np.array(
      [[ True,  True, False, False, False],
       [ True,  True,  True, False, False],
       [False,  True,  True,  True, False],
       [False, False,  True, False, False],
       [False, False,  True, False, False],
       [False,  True,  True,  True, False]])
    
elif 1 <= test_num <= 4: 
    # Load the concrete image and expected answer from the ref file 
    ref_data = np.load('ref_data_' + str(test_num) + '.npz', allow_pickle = True)
    concrete_image = ref_data['concrete_image']
    expected_answer = ref_data['concrete_crack_bool']
    
    # The threshold 
    threshold = threshold_list[test_num]
     
else: 
    print('Not a valid test number')


# %% Run the function and check the answers

# Call the function find_concrete_crack_bool() and store the answer in your_answer
your_answer = find_crack.find_concrete_crack_bool(concrete_image,threshold)

# Do some basic checks before making a comparison 
# These basic checks are: Is it a numpy array? Is dtype bool?
#                         Does it have the correct shape?
# If all these types are correct, then compare the entries 
if type(your_answer) is np.ndarray:
    # your answer is a numpy array
    if your_answer.dtype.name == 'bool':
        # your_answer is a numpy array of bool dtype
        if your_answer.shape == expected_answer.shape:
            # your_answer has the right type and shape
            if np.all(your_answer == expected_answer):
                # All entries are correct
                print('Your answer is correct')
            else: 
                # Not all entries are correct 
                print('Some elements in your answers are incorrect')
                
            # Plot the given concrete image 
            plt.figure()
            plt.imshow(concrete_image, cmap = 'gray', vmin = 0, vmax = 255)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = concrete_image.shape[1]-0.5
            y_min = -0.5
            y_max = concrete_image.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar()
            plt.title('The given image')
            plt.show()

            # Plot your answer
            plt.figure()
            plt.imshow(your_answer, cmap = 'gray', vmin = 0, vmax = 1)
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
            plt.title('Your answer. White: True. Black: False')
            plt.show()
            
            # Plot the expected answer
            plt.figure()
            plt.imshow(expected_answer, cmap = 'gray', vmin = 0, vmax = 1)
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
            plt.title('Expected answer. White: True. Black: False')            
            plt.show()
            
        else:
            print('Your answer has a shape of:',your_answer.shape)
            print('The expected answer has a shape of:',expected_answer.shape)
    else:
        print('Your function output did not return a numpy array of bool type')  
else:
    print('Your function output did not return a numpy array')    
