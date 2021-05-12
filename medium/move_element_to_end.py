# Move Element To End
# You're given an array of integers and an integer. Write a function that moves
# all instances of that integer in the array to the end of the array and returns
# the array.

# The function should perform this in place (i.e., it should mutate the input
# array) and doesn't need to maintain the order of the other integers.

# Sample Input
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2
# Sample Output
# [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

# Solution

def moveElementToEnd(array, toMove):
  start_index = 0
  end_index = len(array) - 1
  while start_index < end_index:
    if array[end_index] == toMove:
      end_index -= 1
    elif array[start_index] != toMove:
      start_index += 1
    else:
      temp = array[start_index]
      array[start_index] = array[end_index]
      array[end_index] = temp
  return array
