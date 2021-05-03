# Monotonic Array
# Write a function that takes in an array of integers and returns a boolean
# representing whether the array is monotonic.

# An array is said to be monotonic if its elements, from left to right, are
# entirely non-increasing or entirely non-decreasing.

# Non-increasing elements aren't necessarily exclusively decreasing; they simply
# don't increase. Similarly, non-decreasing elements aren't necessarily
# exclusively increasing; they simply don't decrease.

# Note that empty arrays and arrays of one element are monotonic.

# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Sample Output
# true

# Solution

def is_monotonic(array):
	increase = 0
	decrease = 0
  for index in range(len(array) - 1):
		if array[index] < array[index + 1]:
			increase += 1
		if array[index] > array[index + 1]:
			decrease += 1
	return False if increase > 0 and decrease > 0 else True
