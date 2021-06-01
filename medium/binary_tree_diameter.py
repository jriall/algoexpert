# Binary Tree Diameter

# Write a function that takes in a Binary Tree and returns its diameter. The
# diameter of a binary tree is defined as the length of its longest path, even
# if that path doesn't pass through the root of the tree.

# A path is a collection of connected nodes in a tree, where no node is
# connected to more than two other nodes. The length of a path is the number of
# edges between the path's first node and its last node.

# Each BinaryTree node has an integer value, a left child node, and a right
# child node. Children nodes can either be BinaryTree nodes themselves or
# None / null.

# Sample Input
# tree =        1
#             /   \
#            3     2
#          /   \ 
#         7     4
#        /       \
#       8         5
#      /           \
#     9             6
# Sample Output
# 6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
# // There are 6 edges between the
# // first node and the last node
# // of this tree's longest path.

# Solution

from dataclasses import dataclass

# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

@dataclass
class TreeInfo:
  diameter: int = 0
  height: int = 0
    

def binaryTreeDiameter(tree):
  return navigate_tree(tree).diameter
  
def navigate_tree(tree):
  if tree is None:
    return TreeInfo()
  left = navigate_tree(tree.left)
  right = navigate_tree(tree.right)
  height = 1 + max([left.height, right.height])
  diameter = left.height + right.height
  new_diameter = max([diameter, left.diameter, right.diameter])
  return TreeInfo(height=height, diameter=new_diameter)