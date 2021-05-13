# Find Three Largest Numbers
# Write a function that takes in an array of at least three integers and,
# without sorting the input array, returns a sorted array of the three largest
# integers in the input array.

# The function should return duplicate integers if necessary; for example, it
# should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

import math

def find_three_largest_numbers(array):
  results = {
    'smallest': -math.inf,
    'middle': -math.inf,
    'largest': -math.inf,
  }
  for num in array:
    if num > results['largest']:
      results['smallest'] = results['middle']
      results['middle'] = results['largest']
      results['largest'] = num
    elif num > results['middle']:
      results['smallest'] = results['middle']
      results['middle'] = num
    elif num > results['smallest']:
      results['smallest'] = num
  return [results['smallest'], results['middle'], results['largest']]
