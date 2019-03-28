'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

# SOLUTION

def calculate_trapped_water(walls):
    if len(walls) < 3:
        return 0

    total_water_volume = 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0

    while left <= right:
        if walls[left] < walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water_volume += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water_volume += right_max - walls[right]
            right -= 1

    return total_water_volume


print(calculate_trapped_water([1])) # 0
print(calculate_trapped_water([2, 1])) # 0
print(calculate_trapped_water([2, 1, 2])) # 1
print(calculate_trapped_water([4, 1, 2])) # 1
print(calculate_trapped_water([4, 1, 2, 3])) # 3
print(calculate_trapped_water([3, 0, 1, 3, 0, 5])) # 8
print(calculate_trapped_water([10, 9, 1, 1, 6]) ) # 0