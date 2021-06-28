# Zigzag Traverse

# Write a function that takes in an n x m two-dimensional array (that can be
# square-shaped when n == m) and returns a one-dimensional array of all the
# array's elements in zigzag order.

# Zigzag order starts at the top left corner of the two-dimensional array, goes
# down by one element, and proceeds in a zigzag pattern all the way to the
# bottom right corner.

# Sample Input
# array = [
#   [1,  3,  4, 10],
#   [2,  5,  9, 11],
#   [6,  8, 12, 15],
#   [7, 13, 14, 16],
# ]
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def zigzagTraverse(array):
  result = []
  i, j = 0, 0
  going_down = True
  while i < len(array) and j < len(array[0]):
    result.append(array[i][j])
    if going_down:
      if i == len(array) - 1:
        j += 1
        going_down = False
      elif j == 0:
        i += 1
        going_down = False
      else:
        i += 1
        j -= 1
    else:
      if j == len(array[0]) - 1:
        i += 1
        going_down = True
      elif i == 0:
        j += 1
        going_down = True
      else:
        j += 1
        i -= 1
  return result
