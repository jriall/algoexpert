# Max Subset Sum No Adjacent

# Write a function that takes in an array of positive integers and returns the
# maximum sum of non-adjacent elements in the array.

# If the input array is empty, the function should return 0.

# Sample Input
# array = [75, 105, 120, 75, 90, 135]
# Sample Output
# 330 // 75 + 120 + 135

# Solution

def maxSubsetSumNoAdjacent(array):
  if len(array) == 0:
    return 0
  if len(array) == 1:
    return array[0]
  prev = array[0]
  curr = max(array[0], array[1])
  for index in range(2, len(array)):
    next = max(curr, array[index] + prev)
    prev = curr
    curr = next
  return curr
