import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in experimental data collected in-class 
df = pd.read_csv('session3_data.csv')

# Convert pandas data frames to arrays (done for you)

# Response times for the upward and downward face stimuli
face_up = df["Trial3"].as_matrix()
face_down = df["Trial1"].as_matrix()

# Response times for the upward and downward object stimuli
obj_up = df["Trial4"].as_matrix()
obj_down = df["Trial2"].as_matrix()

# Implement a function that performs permutation test for group difference (group B mean - group A mean)
# datGrpA is data (e.g. an array) from group A
# datGrpB is data (e.g. an array) from group B
# nperm is number of permutations you'd like to perform
# pvalue is the actual p-value computed from the test

# Your function below should / could follow these steps:


    # step 1 - take the difference in group mean 

    # step 2 - place two groups of data into 1 arracy using "np.concatenate" (Google its usage)

    # step 3 - create an array of zeros as place holder for permuted differences

    # step 4 - iterate over all permuted rounds using a "for" loop
    # at each iteration, randomly permute the array elements in the concatonated array created by step 2
    # use "np.random.permutation" (Google its usage)
    # then take the difference between the means of second and first halves of the permuted array
    # store that difference at each iteration in the array created by step 3

    # step 5 - count how many instances where the value in the permuted differences is greater than the actual difference from step 1
    # e.g. "sum(i>5 for i in a)" calculates number of elements in array "a" that exceeds 5

    # step 6 - compute the p-value by dividing the count from step 5 into the total number of permutations nperm

#####################################
def permtest(datGrpA,datGrpB,nperm):

    return pvalue
#####################################




# Perform permutation test between face_up and face_down groups; set nperm = 10000
# i.e. test if difference in average reaction times of these two groups is significant at p < 0.05

nperm = 10000;


# Similarly, perform permutation test between obj_up and obj_down groups; set nperm = 10000


#print(pvalue_face)
#print(pvalue_object)


# Report the following stats and questions at this link:  http://goo.gl/forms/abdBPeHeoZ 
# p-value for face_up vs face_down (condition 1)
# p-value for obj_up vs obj_down (condition 2)
# Your 1-sentence conclusion for condition 1
# Your 1-sentence conclusion for condition 2
# Your python function for permtest ONLY 

# Bonus point - Is the mean reaction time difference between upright-inverted trials for faces greater than that for objects?
# Apply a permutation test to this proposal and report the p-value; submit the corresponding portion of the python code

#print(pvalue_faceDiff_vs_objDiff)



# At your leisure - histogram-plot the permuted differences and see what they look like (you can do so by returning these difference arrays by modifying slightly the permtest function you wrote)


