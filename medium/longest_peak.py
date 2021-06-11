# Longest Peak

# Write a function that takes in an array of integers and returns the length of
# the longest peak in the array.

# A peak is defined as adjacent integers in the array that are strictly
# increasing until they reach a tip (the highest value in the peak), at which
# point they become strictly decreasing. At least three integers are required to
# form a peak.

# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10
# don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3
# don't form a peak because there aren't any strictly decreasing integers after
# the 3.

# Sample Input
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# Sample Output
# 6 // 0, 10, 6, 5, -1, -3

def longestPeak(array):
  if len(array) < 3:
    return 0
  has_increased = False
  is_increasing = array[1] >= array[0]
  max_peak = 0
  current_peak = 1
  for i in range(1, len(array)):
    if is_increasing:
      if array[i] > array[i - 1]:
        current_peak += 1
      elif array[i] == array[i - 1]:
        current_peak = 1
      else:
        current_peak += 1
        is_increasing = False
        has_increased = array[i- 1] != array[i - 2]
    else:
      if array[i] < array[i - 1]:
        current_peak += 1
      elif array[i] > array[i - 1]:
        if has_increased:
          max_peak = max(max_peak, current_peak)
        current_peak = 2
        is_increasing = True
        has_increased = False
      else:
        if has_increased:
          max_peak = max(max_peak, current_peak)
        current_peak = 1
        is_increasing = True
        has_increased = False
  if not is_increasing and has_increased:
    max_peak = max(max_peak, current_peak)
  return max_peak