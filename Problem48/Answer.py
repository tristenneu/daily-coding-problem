'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''

# SOLUTION 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_char = preorder[0]
    if len(preorder) == 1:
        return Node(root_char)

    root_node = Node(root_char)
    for i, char in enumerate(inorder):
        if char == root_char:
            root_node.left = get_tree(
                preorder=preorder[1:i+1], inorder=inorder[:i])
            root_node.right = get_tree(
                preorder=preorder[i+1:], inorder=inorder[i+1:])

    return root_node

inOrder = ['d', 'b', 'e', 'a', 'f', 'c', 'g'] 
preOrder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
tree = get_tree(preorder=preOrder, inorder=inOrder)

print(tree.val) # 'a'
print(tree.left.val) # 'b'
print(tree.left.left.val) # 'd'
print(tree.left.right.val) # 'e'
print(tree.right.val) # 'c'
print(tree.right.left.val) # 'f'
print(tree.right.right.val) # 'g'