# BST Construction
# Write a BST class for a Binary Search Tree. The class should support:

# Inserting values with the insert method.
# Removing values with the remove method; this method should only remove the 
# first instance of a given value.
# Searching for values with the contains method.
# Note that you can't remove values from a single-node tree. In other words,
# calling the remove method on a single-node tree should simply not do anything.

# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST
# property: its value is strictly greater than the values of every node to its
# left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or None /
# null.

# Solution

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_node = self
    while True:
      if value < current_node.value:
        if current_node.left is None:
          current_node.left = BST(value)
          break
        else:
          current_node = current_node.left
      else:
        if current_node.right is None:
          current_node.right = BST(value)
          break
        else:
          current_node = current_node.right
    return self

  def contains(self, value):
    current_node = self
    while True:
      if value < current_node.value:
        if current_node.left is None:
          return False
        else:
          current_node = current_node.left
      elif value > current_node.value:
        if current_node.right is None:
          return False
        else:
          current_node = current_node.right
      else:
        return True
    return False

  def remove(self, value, parent_node = None):
    current_node = self
    while current_node is not None:
      if value < current_node.value:
        parent_node = current_node
        current_node = current_node.left
      elif value > current_node.value:
        parent_node = current_node
        current_node = current_node.right
      else:
        if current_node.left is not None and current_node.right is not None:
          current_node.value = current_node.right.get_min_value()
          current_node.right.remove(current_node.value, current_node)
        elif parent_node is None:
          if current_node.left is not None:
            current_node.value = current_node.left.value
            current_node.right = current_node.left.right
            current_node.left = current_node.left.left
          elif current_node.right is not None:
            current_node.value = current_node.right.value
            current_node.left = current_node.right.left
            current_node.right = current_node.right.right
          else:
            pass
        elif parent_node.left == current_node:
          parent_node.left = current_node.left if current_node.left is not None else current_node.right
        elif parent_node.right == current_node:
          parent_node.right = current_node.left if current_node.left is not None else current_node.right
        break
    return self
  
  def get_min_value(self):
    current_node = self
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.value