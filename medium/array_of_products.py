# Array of Products

# Write a function that takes in a non-empty array of integers and returns an
# array of the same length, where each element in the output array is equal to
# the product of every other number in the input array.

# In other words, the value at output[i] is equal to the product of every number
# in the input array other than input[i].

# Note that you're expected to solve this problem without using division.

# Sample Input
# array = [5, 1, 4, 2]
# Sample Output
# [8, 40, 10, 20]
# // 8 is equal to 1 x 4 x 2
# // 40 is equal to 5 x 4 x 2
# // 10 is equal to 5 x 1 x 2
# // 20 is equal to 5 x 1 x 4

# Solution

def arrayOfProducts(array):
  left_products = [1]
  left_sum = 1
  for i in range(1, len(array)):
    left_products.append(array[i - 1] * left_sum)
    left_sum = array[i - 1] * left_sum
  j = len(array) - 2
  right_sum = 1
  right_products = [1 for num in array]
  while j >= 0:
    right_products[j] = (array[j + 1] * right_sum)
    right_sum = array[j + 1] * right_sum
    j -= 1
  results = []
  for i in range(len(array)):
    results.append(left_products[i] * right_products[i])
  return results