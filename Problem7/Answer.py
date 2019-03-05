'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

# SOLUTION

def nombre_codage(message):
    map=[]

    for i in range(1,27,1):
        map.append(i)
    nbr=1
    n=len(message)
    pair_couple=0

    for j in range (0,n,2):
        if int(message[j:j+2]) in map and len(message[j:j+2])==2:
            pair_couple+=1

    nbr+=2**pair_couple-1 
    impair_couple=0

    for k in range (1,n,2):
        if int(message[k:k+2]) in map and len(message[k:k+2])==2:
            impair_couple+=1

    nbr+=2**impair_couple-1  

    return nbr 

print(nombre_codage('111'));