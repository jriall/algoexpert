# Shifted Binary Search

# Write a function that takes in a sorted array of distinct integers as well as
# a target integer. The caveat is that the integers in the array have been
# shifted by some amount; in other words, they've been moved to the left or to
# the right by one or more positions. For example, [1, 2, 3, 4] might have
# turned into [3, 4, 1, 2].

# The function should use a variation of the Binary Search algorithm to
# determine if the target integer is contained in the array and should return
# its index if it is, otherwise -1.

# Sample Input
# array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
# target = 33
# Sample Output
# 8

def shiftedBinarySearch(array, target):
  start = 0
  end = len(array) - 1
  while start <= end:
    middle = (start + end) // 2
    if array[middle] == target:
      return middle
    elif array[start] > array[middle]:
      if target > array[middle] and target <= array[end]:
        start = middle + 1
      else:
        end = middle - 1
    else:
      if target < array[middle] and target >= array[start]:
        end = middle - 1
      else:
        start = middle + 1
  return -1