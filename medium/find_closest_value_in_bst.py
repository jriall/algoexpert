# Find Closest Value In BST
# Write a function that takes in a Binary Search Tree (BST) and a target integer
# value and returns the closest value to that target value contained in the BST.

# You can assume that there will only be one closest value.

# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST
# property: its value is strictly greater than the values of every node to its
# left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or None /
# null.

# Sample Input
# tree =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
# target = 12
# Sample Output
# 13

# Solution

def findClosestValueInBst(tree, target):
  current = tree
	closest = tree.value
	while current is not None:
		if abs(target - current.value) < abs(target - closest):
			closest = current.value
		if current.left is not None and target < current.value:
			current = current.left
		else:
			current = current.right
	return closest


# This is the class of the input tree. Do not edit.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
