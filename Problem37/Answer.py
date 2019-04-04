'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

# SOLUTION

# python3 program for power set 

import math; 

def printPowerSet(set,set_size): 
	
	# set_size of power set of a set 
	# with set_size n is (2**n -1) 
	pow_set_size = (int) (math.pow(2, set_size)); 
	counter = 0; 
	j = 0; 
	
	# Run from counter 000..0 to 111..1 
	for counter in range(0, pow_set_size): 
		for j in range(0, set_size): 
			
			# Check if jth bit in the 
			# counter is set If set then 
			# print jth element from set 
			if((counter & (1 << j)) > 0): 
				print(set[j], end = ''); 
		print(''); 

# Driver program to test printPowerSet 
set = [1, 2, 3]; 
printPowerSet(set, 3); 

# This code is contributed by mits. 