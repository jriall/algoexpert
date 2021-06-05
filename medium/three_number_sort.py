# Three Number Sort

# You're given an array of integers and another array of three distinct
# integers. The first array is guaranteed to only contain integers that are in
# the second array, and the second array represents a desired order for the
# integers in the first array. For example, a second array of [x, y, z]
# represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in
# the first array.

# Write a function that sorts the first array according to the desired order in
# the second array.

# The function should perform this in place (i.e., it should mutate the input
# array), and it shouldn't use any auxiliary space (i.e., it should run with
# constant space: O(1) space).

# Note that the desired order won't necessarily be ascending or descending and
# that the first array won't necessarily contain all three integers found in
# the second array—it might only contain one or two.

# Sample Input
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# Sample Output
# [0, 0, 0, 1, 1, 1, -1, -1]

# Solution

def threeNumberSort(array, order):
  counts = {
    order[0]: 0,
    order[1]: 0,
    order[2]: 0,
  }
  for num in array:
    counts[num] += 1
  for index in range(len(array)):
    if counts[order[0]] > 0:
      array[index] = order[0]
      counts[order[0]] -= 1
    elif counts[order[1]] > 0:
      array[index] = order[1]
      counts[order[1]] -= 1
    elif counts[order[2]] > 0:
      array[index] = order[2]
      counts[order[2]] -= 1
  return array