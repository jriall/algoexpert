# Linked List construction

# This is an input class. Do not edit.
class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
  def __init__(self):
      self.head = None
      self.tail = None

  def setHead(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.insertBefore(self.head, node)

  def setTail(self, node):
    if self.tail is None:
      self.setHead(node)
    else:
      self.insertAfter(self.tail, node)

  def insertBefore(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node.prev
    nodeToInsert.next = node
    if node.prev is not None:
      node.prev.next = nodeToInsert
    else:
      self.head = nodeToInsert

  node.prev = nodeToInsert

  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    if node.next is not None:
      node.next.prev = nodeToInsert
    else:
      self.tail = nodeToInsert
    node.next = nodeToInsert

  def insertAtPosition(self, position, nodeToInsert):
    if position == 1:
      self.setHead(nodeToInsert)
      return
    current_pos = 1
    current_node = self.head
    while current_node is not None and current_pos != position:
      current_node = current_node.next
      current_pos += 1
    if current_node is not None:
      self.insertBefore(current_node, nodeToInsert)
    else:
      self.setTail(nodeToInsert)

  def removeNodesWithValue(self, value):
    current_node = self.head
    while current_node is not None:
      node_to_consider = current_node
      current_node = current_node.next
      if node_to_consider.value == value:
        self.remove(node_to_consider)

  def remove(self, node):
    if node == self.tail:
      self.tail = self.tail.prev
    if node == self.head:
      self.head = self.head.next
    self.update_node_pointers(node)

  def update_node_pointers(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    node.prev = None
    node.next = None

  def containsNodeWithValue(self, value):
    current_node = self.head
    while current_node is not None:
      if current_node.value == value:
        return True
      current_node = current_node.next
    return False
