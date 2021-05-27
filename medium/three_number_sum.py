# Three Number Sum

# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. The function should find all triplets in
# the array that sum up to the target sum and return a two-dimensional array of
# all these triplets. The numbers in each triplet should be ordered in
# ascending order, and the triplets themselves should be ordered in ascending
# order with respect to the numbers they hold.

# If no three numbers sum up to the target sum, the function should return an
# empty array.

# Sample Input
# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
# Sample Output
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Solution

def threeNumberSum(array, targetSum):
  result = []    
  array.sort()
  for index in range(len(array) - 2):
    start = index + 1
    end = len(array) - 1
    while start < end:
      sum = array[index] + array[start] + array[end]
      if sum == targetSum:
        result.append([array[index],array[start],array[end]])
        start += 1
        end -= 1
      elif sum < targetSum:
        start += 1
      else:
        end -= 1
  return result
