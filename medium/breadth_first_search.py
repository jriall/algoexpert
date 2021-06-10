# Breadth first search

# You're given a Node class that has a name and an array of optional children
# nodes. When put together, nodes form an acyclic tree-like structure.

# Implement the breadthFirstSearch method on the Node class, which takes in an
# empty array, traverses the tree using the Breadth-first Search approach
# (specifically navigating the tree from left to right), stores all of the
# nodes' names in the input array, and returns it.

# If you're unfamiliar with Breadth-first Search, we recommend watching the
# Conceptual Overview section of this question's video explanation before
# starting to code.

# Sample Input
# graph = A
#    /  |  \
#   B   C   D
#  / \   / \
#   E   F   G   H
#    / \   \
#   I   J   K
# Sample Output
# ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# Solution

class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def breadthFirstSearch(self, array):
    queue = []
    queue.append(self)
    while len(queue):
      current = queue.pop(0)
      for child in current.children:
        queue.append(child)
      array.append(current.name)
    return array

# Solution using deque to avoid O(n) operation with queue.pop(0)

from collections import deque

class Node:
  def __init__(self, name):
    self.children = []
    self.name = name

  def addChild(self, name):
    self.children.append(Node(name))
    return self

  def breadthFirstSearch(self, array):
    queue = deque([self])
    while len(queue) > 0:
      next = queue.popleft()
      for node in next.children:
        queue.append(node)
      array.append(next.name)
    return array
