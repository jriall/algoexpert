# Invert Binary Tree
# Write a function that takes in a Binary Tree and inverts it. In other words,
# the function should swap every left node in the tree for its corresponding
# right node.

# Each BinaryTree node has an integer value, a left child node, and a right
# child node. Children nodes can either be BinaryTree nodes themselves or
# None / null.

# Sample Input
# tree =    1
#        /     \
#       2       3
#     /   \   /   \
#    4     5 6     7
#  /   \
# 8     9
# Sample Output
#        1
#     /     \
#    3       2
#  /   \   /   \
# 7     6 5     4
#             /   \
#            9     8

# Solution

def invert_binary_tree(tree):
  if not tree:
    return None
  if tree.left or tree.right:
    temp = invertBinaryTree(tree.left)
    tree.left = invertBinaryTree(tree.right)
    tree.right = temp
  return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
