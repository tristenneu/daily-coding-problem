'''
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

# SOLUTION

from random import random

def biasedCoin():
   return int(random() < 0.2)

def fairCoin(biasedCoin):
   coin1, coin2 = 0,0
   while coin1 == coin2:
      coin1, coin2 = biasedCoin(), biasedCoin()
   return coin1

print(sum(biasedCoin() for i in range(10000))) # p = 0.2

print(sum(fairCoin(biasedCoin) for i in range(10000))) # p = 0.5