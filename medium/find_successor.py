# Find successor

# Write a function that takes in a Binary Tree (where nodes have an additional
# pointer to their parent node) as well as a node contained in that tree and
# returns the given node's successor.

# A node's successor is the next node to be visited (immediately after the given
# node) when traversing its tree using the in-order tree-traversal technique. A
# node has no successor if it's the last node to be visited in the in-order
# traversal.

# If a node has no successor, your function should return None / null.

# Each BinaryTree node has an integer value, a parent node, a left child node,
# and a right child node. Children nodes can either be BinaryTree nodes
# themselves or None / null.

# Sample Input
# tree = 
#               1
#             /   \
#            2     3
#          /   \ 
#         4     5
#        /       
#       6  
# node = 5   
# Sample Output
# 1
# // This tree's in-order traversal order is:
# // 6 -> 4 -> 2 -> 5 -> 1 -> 3 
# // 1 comes immediately after 5.


# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

# Solution 1 (O(n) time, O(n) space)

def findSuccessor(tree, target):
  result = []
  navigate_tree(tree, result)
  for index in range(len(result) - 1):
    if result[index] == target:
      return result[index + 1]
  return None

def navigate_tree(tree, result):
  if tree is None:
    return
  navigate_tree(tree.left, result)
  result.append(tree)
  navigate_tree(tree.right, result)
  

# Solution 2 (O(h) time, O(1) space)

def findSuccessor(tree, node):
  if node.right is not None:
    return getLeftmostChild(node.right)
  else:
    return getAncestorSuccessor(node)
  
def getLeftmostChild(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def getAncestorSuccessor(node):
  current = node
  while current.parent is not None:
    if current.parent.left == current:
      return current.parent
    else:
      current = current.parent
  return current.parent