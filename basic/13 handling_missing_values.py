'''
np.isnan() - check for NaN values 
'''

import numpy as np

arr = np.array([1, 2, np.nan, 4, 5])
nan_mask = np.isnan(arr)
print("Original array:", arr)
print("NaN mask:", nan_mask)    

print("compare with None: ", arr == None) # False


'''
np.nan_to_num()
replace NaN values with a specific value using 
'''

arr = np.array([1, 2, np.nan, 4, 5])
replaced_arr = np.nan_to_num(arr, nan=0)
# replaced_arr = np.nan_to_num(arr, nan=10)
print("Original array:", arr)
print("Array with NaN replaced:", replaced_arr)


'''
np.isinf() - check for infinite values
managing infinite values
1/0
10**10000 
'''

arr = np.array([1, 2, np.inf, 4, 5, -np.inf])
inf_mask = np.isinf(arr)
print("Original array:", arr)
print("Infinite mask:", inf_mask)

replaced_arr = np.nan_to_num(arr, posinf=999, neginf=-999)
print("Array with infinite values replaced:", replaced_arr)