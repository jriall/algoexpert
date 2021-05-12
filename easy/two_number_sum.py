# Two Number Sum
# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.

# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.

# You can assume that there will be at most one pair of numbers summing up to
# the target sum.

# Solutions

# Brute force solution with nested loops

def two_number_sum(array, target_sum):
  for index, first_number in enumerate(array[:len(array)-1]):
    for second_number in array[index+1:]:
      if first_number + second_number == target_sum:
        return [first_number, second_number]
  return []


# O(n) approach using a hash table as a loopup

def two_number_sum(array, target_sum):
  lookup = {}
  for num in array:
    # True is an arbitrary value - we only care about the keys
    lookup[num] = True
  for num in array:
    target_number = target_sum - num
    if target_number in lookup and target_number is not num:
      return [num, target_number]
  return []


# Refined O(n) approach as a simpliciation to the above.

def two_number_sum(array, target_sum):
    lookup = {}
  for num in array:
    if (target_sum - num in lookup):
      return [target_sum - num,  num]
    # True is an arbitrary value - we only care about the keys
    lookup[num] = True
  return []
