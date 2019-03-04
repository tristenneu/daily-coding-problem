'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

# MY APPROACH

# convert the function to a string
# perform regex on the string to find the arguments
# return the first argument for car
# return the second argument for cdr

# import sys
# from inspect import signature
# import re
# from dill.source import getsource

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# def car(consFunction):
#     # print(signature(consFunction))
#     consFunction()

# def getArgs(consFunction):
#     s = getsource(consFunction)
#     print(s)
#     fn_match = re.match(r"(?P<function>\w+)\s?\((?P<arg>(?P<args>\w+(,\s?)?)+)\)", s)
#     print(fn_match)
#     fn_dict = fn_match.groupdict()
#     del fn_dict['args']
#     fn_dict['arg'] = [arg.strip() for arg in fn_dict['arg'].split(',')]
#     print(fn_dict)


# car(cons(3, 4)) # returns 3
# cdr(cons(3, 4)) # returns 4
# getArgs(cons(3, 4))

# SOLUTION

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

print(car(cons(3,4)))
print(cdr(cons(3,4)))