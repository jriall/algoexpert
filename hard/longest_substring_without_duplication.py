# Longest Substring Without Duplication

# Write a function that takes in a string and returns its longest substring
# without duplicate characters.

# You can assume that there will only be one longest substring without
# duplication.

# Sample Input
# string = "clementisacap"
# Sample Output
# "mentisac"

# Solution

def longestSubstringWithoutDuplication(string):
  result = string[0]
  for i in range(len(string) - 1):
    j = i + 1
    seen = {}
    seen[string[i]] = True
    while j < len(string):
      if string[j] in seen:
        break
      else:
        seen[string[j]] = True
        j += 1
    if j - i > len(result):
      result = string[i:j]
  return result