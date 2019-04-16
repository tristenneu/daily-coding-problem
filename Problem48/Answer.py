'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

# SOLUTION

# Python program to find maximum contiguous subarray 

# Function to find the maximum contiguous subarray 
def max_subarray(arr):
    max_ending = max_current = arr[0]

    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)

    return max_current

array1 = [34, -50, 42, 14, -5, 86]
array2 = [-5, -1, -8, -9]
print(max_subarray(array1)) # 137
print(max_subarray(array2)) # 0

