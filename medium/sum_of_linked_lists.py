# Sum of Linked Lists

# You're given two Linked Lists of potentially unequal length. Each Linked List
# represents a non-negative integer, where each node in the Linked List is a
# digit of that integer, and the first node in each Linked List always
# represents the least significant digit of the integer. Write a function that
# returns the head of a new Linked List that represents the sum of the integers
# represented by the two input Linked Lists.

# Each LinkedList node has an integer value as well as a next node pointing to
# the next node in the list or to None / null if it's the tail of the list. The
# value of each LinkedList node is always in the range of 0 - 9.

# Note: your function must create and return a new Linked List, and you're not
# allowed to modify either of the input Linked Lists.

# Sample Input
# linkedListOne = 2 -> 4 -> 7 -> 1
# linkedListTwo = 9 -> 4 -> 5
# Sample Output
# 1 -> 9 -> 2 -> 2
# // linkedListOne represents 1742
# // linkedListTwo represents 549
# // 1742 + 549 = 2291

# Solution

# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
	number_one = sum_of_linked_list(linkedListOne)
	number_two = sum_of_linked_list(linkedListTwo)
	sum = number_one + number_two
	sum_str = str(sum)
	current_node = None
	for string in sum_str:
		new_head = LinkedList(int(string))
		new_head.next = current_node
		current_node = new_head
	return current_node


def sum_of_linked_list(node):
	result = []
	current_node = node
	while current_node is not None:
		result.insert(0, str(current_node.value))
		current_node = current_node.next
	return int(''.join(result))
