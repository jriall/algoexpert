# Longest Substring Without Duplication

# Write a function that takes in a string and returns its longest substring
# without duplicate characters.

# You can assume that there will only be one longest substring without
# duplication.

# Sample Input
# string = "clementisacap"
# Sample Output
# "mentisac"

# Infficient Solution O(n^2) time, O(n) space

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

# O(n) time, O(n) space solution

def longestSubstringWithoutDuplication(string):
  seen = {}
  result = {'start': 0, 'end': 1}
  start = 0
  for index, char in enumerate(string):
    if char in seen:
      start = max(start, seen[char] + 1)
    if result['end'] - result['start'] < index + 1 - start:
      result = {
        'start': start,
        'end': index + 1,
      }
    seen[char] = index
  return string[result['start']:result['end']]
