# Max Path Sum In Binary Tree

# Write a function that takes in a Binary Tree and returns its max path sum.

# A path is a collection of connected nodes in a tree, where no node is
# connected to more than two other nodes; a path sum is the sum of the values of
# the nodes in a particular path.

# Each BinaryTree node has an integer value, a left child node, and a right
# child node. Children nodes can either be BinaryTree nodes themselves or
# None / null.

# Sample Input
# tree = 1
#     /     \
#    2       3
#  /   \   /   \
# 4     5 6     7
# Sample Output
# 18 // 5 + 2 + 1 + 3 + 7

def maxPathSum(tree):
  return max(get_max_sum(tree))

def get_max_sum(tree):
  if tree is None:
    return (float('-inf'), float('-inf'))
  left_branch_sum, left_sum = get_max_sum(tree.left)
  right_branch_sum, right_sum = get_max_sum(tree.right)
  max_child_branch_sum = max(left_branch_sum, right_branch_sum)
  max_branch_sum = max(max_child_branch_sum + tree.value, tree.value)
  max_sum_triangle = max(max_branch_sum, left_branch_sum + tree.value + right_branch_sum)
  running_max_path_sum = max(left_sum, right_sum, max_sum_triangle)
  return (running_max_path_sum, max_branch_sum)