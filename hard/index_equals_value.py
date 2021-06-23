# Index Equals Zero

# Write a function that takes in a sorted array of distinct integers and returns
# the first index in the array that is equal to the value at that index. In
# other words, your function should return the minimum index where
# index == array[index].

# If there is no such index, your function should return -1.

# Sample Input
# array = [-5, -3, 0, 3, 4, 5, 9]
# Sample Output
# 3 // 3 == array[3]

def indexEqualsValue(array):
  start = 0
  end = len(array) - 1
  while start <= end:
    middle = (end + start) // 2
    if array[middle] < middle:
      start = middle + 1
    elif array[middle] == middle and middle == 0:
      return 0
    elif array[middle] == middle and array[middle - 1] != middle - 1:
      return middle
    else:
      end = middle - 1
  return -1
