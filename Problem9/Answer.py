'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

# SOLUTION

# Function to return max sum such that  
# no two elements are adjacent 
def find_max_sum(arr): 
    incl = 0
    excl = 0
     
    for i in arr: 
          
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = excl if excl>incl else incl 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (excl if excl>incl else incl)

# Driver program to test above function 
arr1 = [2, 4, 6, 2, 5]
arr2 = [5, 1, 1, 5]
print(find_max_sum(arr1)) # 13
print(find_max_sum(arr2)) # 10  
# This code is contributed by Kalai Selvan