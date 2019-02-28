'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

# iterative approach
# find list of factors excluding the index
# multiply the list together, save the result
# return array of products

from functools import reduce

def findProducts(list):
    products = []

    for index in range(len(list)):
        factors = [list[factor] for factor in range(len(list)) if factor != index]
        print(factors)
        product = reduce(lambda x,y:x*y, factors)
        print(product)
        products.append(product)
    
    print(products)

findProducts([1, 2, 3, 4, 5]) # [120, 60, 40, 30, 24]
findProducts([3, 2, 1]) # [2, 3, 6]