'''
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

# SOLUTION

def find_element(arr, element, start, end):

    if start == end:
        return

    mid = start + ((end - start) // 2)

    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        if arr[start] >= element:
            return find_element(arr, element, start, mid)
        else:
            return find_element(arr, element, mid, end)
    elif arr[mid] < element:
        if arr[start] <= element:
            return find_element(arr, element, start, mid)
        else:
            return find_element(arr, element, mid, end)


def find_element_main(arr, element):
    element_pos = find_element(arr, element, 0, len(arr))
    return element_pos


print(find_element_main([13, 18, 25, 2, 8, 10], 2)) # 3
print(find_element_main([13, 18, 25, 2, 8, 10], 8)) # 4
print(find_element_main([25, 2, 8, 10, 13, 18], 8)) # 2
print(find_element_main([8, 10, 13, 18, 25, 2], 8)) # 0