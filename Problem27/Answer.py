'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

# SOLUTION

def pairs_stack(string, pairs = {'[': ']', '{': '}', '(': ')'}):

    opening = list(pairs.keys())

    closing = list(pairs.values())

    match = list()

    for s in string:
        if s in opening:
            match.insert(0, s)
        elif s in closing:
            if len(match) == 0:
                return False
            if match[0] == opening[closing.index(s)]:
                match.pop(0)
            else:
                return False

    if len(match) == 0:
        return True

    return False

string1 = '([])[]({})'
string2 = '([)]'
string3 = '((()'
print(pairs_stack(string1))
print(pairs_stack(string2))
print(pairs_stack(string3))