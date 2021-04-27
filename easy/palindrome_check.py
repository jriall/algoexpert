# Palindrome Check
# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.

# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes.

import math

def isPalindrome(string):
	# We only need to iterate through half of the string (excluding the middle
	# letter if present) to match against the corresponding paired letter in
	# the second half of the string.
  for index in range(math.floor(len(string) / 2)):
  if string[index] is not string[len(string) - index - 1]:
    return False
	return True
