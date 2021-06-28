# Min Heap Construction

# Implement a MinHeap class that supports:

# Building a Min Heap from an input array of integers.
# Inserting integers in the heap.
# Removing the heap's minimum / root value.
# Peeking at the heap's minimum / root value.
# Sifting integers up and down the heap, which is to be used when inserting and
# removing values.
# Note that the heap should be represented in the form of an array.

# Sample Usage
# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

# // All operations below are performed sequentially.
# MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and
# populates the heap)
# buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
# peek(): -5
# remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
# peek(): 2
# remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
# peek(): 6
# insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]

# Solution

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]


class MinHeap:
  def __init__(self, array):
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    parent_index = (len(array) - 2) // 2
    while parent_index >= 0:
      self.siftDown(parent_index, array)
      parent_index -= 1
    return array

  def siftDown(self, current_index, heap):
    end_index = len(heap) - 1
    child_one_index = current_index * 2 + 1
    while child_one_index <= end_index:
      child_two_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else - 1
      if child_two_index != -1 and heap[child_two_index] < heap[child_one_index]:
        index_to_swap = child_two_index
      else:
        index_to_swap = child_one_index
      if heap[index_to_swap] < heap[current_index]:
        swap(heap, current_index, index_to_swap)
        current_index = index_to_swap
        child_one_index = current_index * 2 + 1
      else:
        break

  def siftUp(self, current_index):
    parent_index = (current_index - 1) // 2
    while current_index > 0 and self.heap[current_index] < self.heap[parent_index]:
      swap(self.heap, parent_index, current_index)
      current_index = parent_index
      parent_index = (current_index - 1) // 2

  def peek(self):
    if len(self.heap):
      return self.heap[0]
    else:
      return None

  def remove(self):
    swap(self.heap, 0, len(self.heap) - 1)
    value = self.heap.pop()
    self.siftDown(0, self.heap)
    return value

  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1)