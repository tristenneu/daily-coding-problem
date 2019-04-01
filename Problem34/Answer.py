'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

# SOLUTION

def is_palindrome(s):
    return s[::-1] == s


def get_nearest_palindrome(s):

    if is_palindrome(s):
        return s

    if s[0] == s[-1]:
        return s[0] + get_nearest_palindrome(s[1:-1]) + s[-1]
    else:
        pal_1 = s[0] + get_nearest_palindrome(s[1:]) + s[0]
        pal_2 = s[-1] + get_nearest_palindrome(s[:-1]) + s[-1]

        if len(pal_1) > len(pal_2):
            return pal_2
        elif len(pal_1) < len(pal_2):
            return pal_1
        return pal_1 if pal_1 < pal_2 else pal_2


print(get_nearest_palindrome('racecar')) # 'racecar'
print(get_nearest_palindrome('google')) # 'elgoogle'
print(get_nearest_palindrome('egoogle')) # 'elgoogle'
print(get_nearest_palindrome('elgoog')) # 'elgoogle'
print(get_nearest_palindrome('race')) # 'ecarace'