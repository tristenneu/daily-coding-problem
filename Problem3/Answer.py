'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

# add serialize and deserialize to the class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def serialize(root):
    level_list = []
    current_level = [root]
    while current_level:
        level_list.append(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level
    print(level_list)
    treesting = ', '.join(level_list)
    print(treesting)

def deserialize(s):
    container = [None]
    leaves = [[container, 0]] # put the reference to the root on the queue

    for val in s.split(', '):
        children, childIndex = leaves.pop(0) # pull from queue
        node = children[childIndex] = {
                'val': val,
                'children': [None, None]
            }
        # append the new 2 child references to the queue
        leaves.append([node['children'], 0])
        leaves.append([node['children'], 1])
        if len(leaves) == 0: # should not happen if input is complete
            break 

    # print(container[0]) # return the root
    print(container[0]['children'][1]['val'])


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
deserialize('root, left right, left.left')
# assert deserialize(serialize(node)).left.left.val == 'left.left'