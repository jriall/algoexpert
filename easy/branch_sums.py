# Branch Sums
# Write a function that takes in a Binary Tree and returns a list of its branch
# sums ordered from leftmost branch sum to rightmost branch sum.

# A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
# branch is a path of nodes in a tree that starts at the root node and ends at
# any leaf node.

# Each BinaryTree node has an integer value, a left child node, and a right
# child node. Children nodes can either be BinaryTree nodes themselves or None
# / null.

# Sample Input
# tree =     1
#         /     \
#        2       3
#      /   \    /  \
#     4     5  6    7
#   /   \  /
#  8    9 10
# Sample Output
# [15, 16, 18, 10, 11]
# // 15 == 1 + 2 + 4 + 8
# // 16 == 1 + 2 + 4 + 9
# // 18 == 1 + 2 + 5 + 10
# // 10 == 1 + 3 + 6
# // 11 == 1 + 3 + 7

# Solution

class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def branchSums(root):
  result = []
  navigate_branch(root, 0, result)
  return result

def navigate_branch(root, branch_total, result):
  new_branch_total = branch_total + root.value
  if root.left:
    navigate_branch(root.left, new_branch_total, result)
  if root.right:
    navigate_branch(root.right, new_branch_total, result)
  if not root.left and not root.right:
    result.append(new_branch_total)
