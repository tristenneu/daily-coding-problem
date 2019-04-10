'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

# SOLUTION

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val > self.stack[self.max_stack[-1]]:
            self.max_stack.append(len(self.stack) - 1)

    def pop(self):
        if not self.stack:
            return None
        if len(self.stack) - 1 == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        if not self.stack:
            return None
        return self.stack[self.max_stack[-1]]


s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
print(s.max()) # 5
s.pop()
print(s.max()) # 3
s.pop()
print(s.max()) # 3
s.pop()
print(s.max()) # 1
s.pop()
print(s.max()) # None

s = Stack()
s.push(10)
s.push(3)
s.push(2)
s.push(5)
print(s.max()) # 10
s.pop()
print(s.max()) # 10
s.pop()
print(s.max()) # 10
s.pop()
print(s.max()) # 10
s.pop()
print(s.max()) # None