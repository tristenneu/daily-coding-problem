'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

# iterative approach
# bubble sort for o(n) time and o(1) space
# loop through sorted array and find difference for lowest positive integer
# store answer in a variable

# MY APPROACH

# import itertools as it
# from functools import reduce

# def missingPositiveInt(list):

#     # bubble sort
#     cmpcount, swapcount = 0, 0
#     n = 0

#     while n < len(list) - 1:
#         cmpcount += 1
#         if list[n] > list[n + 1]:
#             swapcount += 1
#             list[n], list[n+1] = list[n+1], list[n]
#             n = 0
#         else:
#             n = n + 1

#     print(list, cmpcount, swapcount)

#     # # find difference between two lowest positive integers
#     # list = [list[i+1]-list[i] for i in range(len(list)-1) if list[i] > 0]
#     answer = 1 + reduce(lambda x, y: x if y-x>1 else y, list, 0)

#     print(answer)

#     # print(list)


# missingPositiveInt([3, 4, -1, 1]) # 2
# missingPositiveInt([1, 2, 0]) # 3

# SOLUTION

def solution(A):#Our original array 
  
    m = max(A) #Storing maximum value 
    if m < 1: 
          
        # In case all values in our array are negative 
        return 1 
    if len(A) == 1: 
          
        #If it contains only one element 
        return 2 if A[0] == 1 else 1     
    l = [0] * m 
    for i in range(len(A)): 
        if A[i] > 0: 
            if l[A[i] - 1] != 1: 
                  
                #Changing the value status at the index of our list 
                l[A[i] - 1] = 1 
    for i in range(len(l)): 
          
        #Encountering first 0, i.e, the element with least value 
        if l[i] == 0:  
            return i+1
            #In case all values are filled between 1 and m 
    return i+2     

solution([3, 4, -1, 1]) # 2
solution([1, 2, 0]) # 3