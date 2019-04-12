'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

# SOLUTION

import numpy
def rand1_5():
    return numpy.random.randint(5)+1

def rand1_7():
    q = 0
    for i in range(7):  
        q += rand1_5()
    return q%7 + 1

print(rand1_5())
print(rand1_7())