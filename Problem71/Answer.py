'''
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''

# SOLUTION

from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    i = 5*rand5() + rand5() - 5  # uniformly samples between 1-25
    if i < 22:
        return i % 7 + 1
    return rand7()