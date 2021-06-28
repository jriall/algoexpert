# Search For Range
# Write a function that takes in a sorted array of integers as well as a target
# integer. The function should use a variation of the Binary Search algorithm to
# find a range of indices in between which the target number is contained in the
# array and should return this range in the form of an array.

# The first number in the output array should represent the first index at which
# the target number is located, while the second number should represent the
# last index at which the target number is located. The function should return
# [-1, -1] if the integer isn't contained in the array.

# If you're unfamiliar with Binary Search, we recommend watching the Conceptual
# Overview section of the Binary Search question's video explanation before
# starting to code.

# Sample Input
# array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# target = 45
# Sample Output
# [4, 9]

def searchForRange(array, target):
  left = do_binary_search(array, target)
  right = do_binary_search(array, target, False)
  return [left, right]

def do_binary_search(array, target, seek_start = True):
  start = 0
  end = len(array) - 1
  while start <= end:
    middle = (start + end) // 2
    if array[middle] == target:
      if middle == 0 or middle == len(array) - 1:
        return middle
      elif array[middle - 1] == target and seek_start:
        end = middle - 1
      elif array[middle + 1] == target and not seek_start:
        start = middle + 1
      else:
        return middle
    elif array[middle] > target:
      end = middle - 1
    else:
      start = middle + 1
  return -1