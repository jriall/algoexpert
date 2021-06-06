# Youngest Common Ancestor

# You're given three inputs, all of which are instances of an AncestralTree
# class that have an ancestor property pointing to their youngest ancestor. The
# first input is the top ancestor in an ancestral tree (i.e., the only instance
# that has no ancestor--its ancestor property points to None / null), and the
# other two inputs are descendants in the ancestral tree.

# Write a function that returns the youngest common ancestor to the two
# descendants.

# Note that a descendant is considered its own ancestor. So in the simple
# ancestral tree below, the youngest common ancestor to nodes A and B is node A.

# // The youngest common ancestor to nodes A and B is node A.
#   A
#  /
# B
# Sample Input
# // The nodes are from the ancestral tree below.
# topAncestor = node A
# descendantOne = node E
# descendantTwo = node I
#           A
#        /     \
#       B       C
#     /   \   /   \
#    D     E F     G
#  /   \
# H     I
# Sample Output
# node B

# Solution

# This is an input class. Do not edit.
class AncestralTree:
  def __init__(self, name):
    self.name = name
    self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
  descendant_one_depth = get_depth(topAncestor, descendantOne)
  descendant_two_depth = get_depth(topAncestor, descendantTwo)
  current_descendant_one = descendantOne
  current_descendant_two = descendantTwo
  while current_descendant_one is not current_descendant_two:
    if descendant_one_depth > descendant_two_depth:
      descendant_one_depth -= 1
      current_descendant_one = current_descendant_one.ancestor
    elif descendant_one_depth < descendant_two_depth:
      descendant_two_depth -= 1
      current_descendant_two = current_descendant_two.ancestor
    else:
      current_descendant_two = current_descendant_two.ancestor
      current_descendant_one = current_descendant_one.ancestor
  return current_descendant_one


def get_depth(topAncestor, descendant):
  curr = descendant
  count = 0
  while curr is not topAncestor:
    curr = curr.ancestor
    count += 1
  return count
