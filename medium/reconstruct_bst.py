# Reconstruct BST

# The pre-order traversal of a Binary Tree is a traversal technique that starts
# at the tree's root node and visits nodes in the following order:

# Current node
# Left subtree
# Right subtree
# Given a non-empty array of integers representing the pre-order traversal of a
# Binary Search Tree (BST), write a function that creates the relevant BST and
# returns its root node.

# The input array will contain the values of BST nodes in the order in which
# these nodes would be visited with a pre-order traversal.

# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST
# property: its value is strictly greater than the values of every node to its
# left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or
# None / null.

# Sample Input
# preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
# Sample Output
#         10
#       /    \
#      4      17
#    /   \      \
#   2     5     19
#  /           /
# 1           18

# This is an input class. Do not edit.
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


# Solution


def reconstructBst(preorder):
	if not preorder:
		return None
	right_child = 1
	while right_child <= len(preorder) - 1 and preorder[right_child] < preorder[0]:
		right_child += 1
	left_subtree = preorder[1:right_child]
	right_subtree = preorder[right_child:]
	root = BST(preorder[0])
	root.left = reconstructBst(left_subtree)
	root.right = reconstructBst(right_subtree)
	return root
