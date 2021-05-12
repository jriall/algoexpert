# Binary Search
# Write a function that takes in a sorted array of integers as well as a target
# integer. The function should use the Binary Search algorithm to determine if
# the target integer is contained in the array and should return its index if it
# is, otherwise -1.

def binary_search(array, target):
  start_pointer = 0
  end_pointer = len(array) - 1
  while start_pointer <= end_pointer:
    middle_pointer = round((end_pointer + start_pointer) / 2)
    if array[middle_pointer] == target:
      return middle_pointer
    elif array[middle_pointer] > target:
      end_pointer = middle_pointer - 1
    else:
      start_pointer = middle_pointer + 1
  return -1
