# Quick Sort

# Solution

def quickSort(array):
  sort_by_pivot(array, 0, len(array) - 1)
  return array

def sort_by_pivot(array, start_index, end_index):
  if start_index >= end_index:
    return
  pivot = start_index
  left = start_index + 1
  right = end_index
  while left <= right:
    if array[left] > array[pivot] and array[right] < array[pivot]:
      swap(array, left, right)
    if array[right] >= array[pivot]:
      right -= 1
    if array[left] <= array[pivot]:
      left += 1
  swap(array, pivot, right)
  left_size = right - 1 - start_index
  right_size = end_index - (right + 1)
  left_is_smaller = left_size < right_size
  if left_is_smaller:
    sort_by_pivot(array, start_index, right - 1)
    sort_by_pivot(array, right + 1, end_index)
  else:
    sort_by_pivot(array, right + 1, end_index)
    sort_by_pivot(array, start_index, right - 1)
  
def swap(array, i, j):
  array[i], array[j] = array[j], array[i]