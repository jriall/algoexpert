# Validate BST
# Write a function that takes in a potentially invalid Binary Search Tree (BST)
# and returns a boolean representing whether the BST is valid.

# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST
# property: its value is strictly greater than the values of every node to its
# left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or None /
# null.

# A BST is valid if and only if all of its nodes are valid BST nodes.

# Sample Input
# tree =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
# Sample Output
# True

# Solution

# This is an input class. Do not edit.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def validateBst(tree):
  return validate_node_helper(tree, float('-inf'), float('inf'))

def validate_node_helper(node, min, max):
	if node is None:
		return True
	if node.value >= max or node.value < min:
		return False
	left_node_is_valid = validate_node_helper(node.left, min, node.value)
	right_node_is_valid = validate_node_helper(node.right, node.value, max)
	return left_node_is_valid and right_node_is_valid
