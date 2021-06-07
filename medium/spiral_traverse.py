# Spiral Traverse

# Write a function that takes in an n x m two-dimensional array (that can be
# square-shaped when n == m) and returns a one-dimensional array of all the
# array's elements in spiral order.

# Spiral order starts at the top left corner of the two-dimensional array, goes
# to the right, and proceeds in a spiral pattern all the way until every element
# has been visited.

# Sample Input
# array = [
#   [1,   2,  3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10,  9,  8, 7],
# ]
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Solution

def spiralTraverse(array):
  result = []
  start_row = 0
  start_col = 0
  end_row = len(array) - 1
  end_col = len(array[0]) - 1
  while start_row <= end_row and start_col <= end_col:
    for index in range(start_col, end_col + 1):
      result.append(array[start_row][index])
    for index in range(start_row + 1, end_row + 1):
      result.append(array[index][end_col])
    if start_row != end_row:
      for index in reversed(range(start_col, end_col)):
        result.append(array[end_row][index])
    if end_col != start_col:
      for index in reversed(range(start_row + 1, end_row)):
        result.append(array[index][start_col])
    start_row += 1
    start_col += 1
    end_row -= 1
    end_col -= 1
  return result