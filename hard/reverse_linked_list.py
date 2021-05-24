# Reverse a linked list

# Solution

class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def reverseLinkedList(head):
  prev = None
  curr = head
  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev