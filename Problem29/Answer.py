'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

# SOLUTION

# Python code for run length encoding 
from collections import OrderedDict 
def runLengthEncoding(input): 

	# Generate ordered dictionary of all lower 
	# case alphabets, its output will be 
	# dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0} 
	dict=OrderedDict.fromkeys(input, 0) 

	# Now iterate through input string to calculate 
	# frequency of each character, its output will be 
	# dict = {'w':4,'a':3,'d':1,'e':1,'x':6} 
	for ch in input: 
		dict[ch] += 1

	# now iterate through dictionary to make 
	# output string from (key,value) pairs 
	output = '' 
	for key,value in dict.items(): 
		output = output + key + str(value) 
	return output 

# Driver function 
if __name__ == "__main__": 
	input='wwwwaaadexxxxxx'
	print(runLengthEncoding(input))
