# Find Kth Largest Value In BST
# Write a function that takes in a Binary Search Tree (BST) and a positive
# integer k and returns the kth largest integer contained in the BST.

# You can assume that there will only be integer values in the BST and that k is
# less than or equal to the number of nodes in the tree.

# Also, for the purpose of this question, duplicate integers will be treated as
# distinct values. In other words, the second largest value in a BST containing
# values {5, 7, 7} will be 7—not 5.

# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST
# property: its value is strictly greater than the values of every node to its
# left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or None /
# null.

# Sample Input
# tree =   15
#        /     \
#       5      20
#     /   \   /   \
#    2     5 17   22
#  /   \         
# 1     3       
# k = 3
# Sample Output
# 17

# Initial O(n) time solution
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
  
def inOrderTraverse(tree, array):
  if tree.left is not None:
    inOrderTraverse(tree.left, array)
  array.append(tree.value)
  if tree.right is not None:
    inOrderTraverse(tree.right, array)
  return array


def findKthLargestValueInBst(tree, k):
  array = []
  inOrderTraverse(tree, array)
  return array[-k]


# Improved time complexity solution
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
  
def reverseInOrderTraverse(tree, array, k):
  if len(array) < k:
    if tree.right is not None:
      reverseInOrderTraverse(tree.right, array, k)
    array.append(tree.value)
    if tree.left is not None:
      reverseInOrderTraverse(tree.left, array, k)
  else:
    return


def findKthLargestValueInBst(tree, k):
  array = []
  reverseInOrderTraverse(tree, array, k)
  if k > len(array):
    return - 1
  else:
    return array[k - 1]
