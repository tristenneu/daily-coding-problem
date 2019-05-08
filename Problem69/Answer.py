'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

# SOLUTION

# A Python3 program to find a maximum 
# product of a triplet in an array of integers 

# Function to find a maximum product of a 
# triplet in array of integers of size n 
def maxProduct(arr, n): 

	# if size is less than 3, no triplet exists 
	if n < 3: 
		return -1

	# Sort the array in ascending order 
	arr.sort() 

	# Return the maximum of product of last 
	# three elements and product of first 
	# two elements and last element 
	return max(arr[0] * arr[1] * arr[n - 1], 
			arr[n - 1] * arr[n - 2] * arr[n - 3]) 

# Driver Code 
if __name__ == '__main__': 

	arr = [-10, -10, 5, 2] 
	n = len(arr) 

	_max = maxProduct(arr, n) 

	if _max == -1: 
		print('No Triplet Exists') 
	else: 
		print('Maximum product is', _max) 

# This code is contributed by Rituraj Jain 