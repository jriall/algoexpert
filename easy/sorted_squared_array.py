# Sorted Squared Array
# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.

# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]

# Brute force solution O(n log n)

def sorted_squared_array(array):
  squares = [n * n for n in array]
  squares.sort()
  return squares

# Optimal force solution O(n)

def sorted_squared_array(array):
  result = []
  largest_index = len(array) - 1
  smallest_index = 0
  while smallest_index <= largest_index:
    largest_square = array[largest_index] * array[largest_index]
    smallest_square = array[smallest_index] * array[smallest_index]
    if largest_square > smallest_square:
      result.insert(0, largest_square)
      largest_index -= 1
    else:
      result.insert(0, smallest_square)
      smallest_index += 1
  return result
