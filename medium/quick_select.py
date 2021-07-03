# Quick Select

# Write a function that takes in an array of distinct integers as well as an
# integer k and that returns the kth smallest integer in that array.

# The function should do this in linear time, on average.

# Sample Input
# array = [8, 5, 2, 9, 7, 6, 3]
# k = 3
# Sample Output
# 5

# Solution

def quickselect(array, k):
  return quickselect_helper(array, 0, len(array) - 1, k)


def quickselect_helper(array, start_index, end_index, k):
  while True:
    pivot = start_index
    left = start_index + 1
    right = end_index
    while left <= right:
      if array[left] > array[pivot] and array[right] < array[pivot]:
        swap(array, left, right)
      if array[left] <= array[pivot]:
        left += 1
      if array[right] >= array[pivot]:
        right -= 1
    swap(array, pivot, right)
    if right > k - 1:
      end_index = right - 1
    elif right < k - 1:
      start_index = right + 1
    else:
      return array[right]


def swap(array, i, j):
  array[j], array[i] = array[i], array[j]