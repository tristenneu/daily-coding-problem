'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

# SOLUTION

def longestPalindrome(s):
  if (not s or len(s) <= 1):
    return s
  longest = s[0:1]
  for i in range(len(s)):
    temp = expand(s, i, i)
    if (len(temp) > len(longest)):
      longest = temp
    temp = expand(s, i, i + 1)
    if (len(temp) > len(longest)):
      longest = temp
  return longest

def expand(s, begin, end):
  while (begin >= 0 and end <= len(s) - 1 and s[begin] == s[end]):
    begin -= 1
    end += 1
  return s[begin+1:end]

print(longestPalindrome("aabcdcb")) # "bcdcb"
print(longestPalindrome("bananas")) # "anana"