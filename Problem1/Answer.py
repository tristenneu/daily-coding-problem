'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

# approach the problem iteratively
# calculate combinations of equations and compare against k
# return the first instance of numbers that add up to k

# import pdb; pdb.set_trace()

def calculateK(numberList, k):
    nums = []

    # iteratively
    for num in range(len(numberList)):
        # print(numberList[num])
        #calculate combinations
        # newNumberList = list(filter(lambda new: new != num, numberList))
        addens = [numberList[new] for new in range(len(numberList)) if new != num]
        # print(addens)
        for index in range(len(addens)):
                eq = numberList[num] + addens[index]

                if eq == k:
                        nums.append(numberList[num])
                        nums.append(addens[index])
                        print(nums)
                        print('True')
                        return True
                else:
                        continue
    print(nums)
    if len(nums) == 0:
            print('False')
            return False
    
# calculateK([10, 15, 3, 7], 17)
calculateK([11, 16, 8, 21], 27)
calculateK([15, 6, 19, 5], 42)