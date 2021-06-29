# Longest Palindromic Substring

# Write a function that, given a string, returns its longest palindromic
# substring.

# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes.

# You can assume that there will only be one longest palindromic substring.

# Sample Input
# string = "abaxyzzyxf"
# Sample Output
# "xyzzyx"

# Solution

def longestPalindromicSubstring(string):
  if len(string) < 2:
    return string
  result = ''
  for index in range(len(string) - 1):
    odd = checkForPalindrome(string, index)
    even = checkForPalindrome(string, index, True)
    if len(odd) > len(result):
      result = odd
    if len(even) > len(result):
      result = even
  return result
    
    
def checkForPalindrome(string, index, checkEvens = False):
  left = index
  right = index + 1 if checkEvens else index
  if string[left] != string[right]:
    return ''
  while left >= 0 and right < len(string):
    if string[left] != string[right]:
      break
    else:
      left -= 1
      right += 1
  return string[left + 1:right]