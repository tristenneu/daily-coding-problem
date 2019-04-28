'''
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

# SOLUTION

# Python3 code for extended version 
# of power function that can work 
# for float x and negative y 

def power(x, y): 

	if(y == 0): return 1
	temp = power(x, int(y / 2)) 
	
	if (y % 2 == 0): 
		return temp * temp 
	else: 
		if(y > 0): return x * temp * temp 
		else: return (temp * temp) / x 
	
# Driver Code 
x, y = 2, 10
print('%.6f' %(power(x, y))) # 1024

# This code is contributed by Smitha Dinesh Semwal. 