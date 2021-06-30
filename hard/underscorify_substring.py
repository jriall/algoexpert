# Underscorify Substring

# Write a function that takes in two strings: a main string and a potential
# substring of the main string. The function should return a version of the main
# string with every instance of the substring in it wrapped between underscores.

# If two or more instances of the substring in the main string overlap each
# other or sit side by side, the underscores relevant to these substrings should
# only appear on the far left of the leftmost substring and on the far right of
# the rightmost substring. If the main string doesn't contain the other string
# at all, the function should return the main string intact.

# Sample Input
# string = "testthis is a testtest to see if testestest it works"
# substring = "test"
# Sample Output
# "_test_this is a _testtest_ to see if _testestest_ it works"

# Solution

def underscorifySubstring(string, substring):
  matches = []
  for index in range(len(string) - len(substring) + 1):
    end = index + len(substring)
  if string[index:end] == substring:
    matches.append([index, end])
  if len(matches) == 0:
    return string
  collapsed_matches = [matches[0]]
  for index in range(1, len(matches)):
    if matches[index][0] <= collapsed_matches[-1][1]:
      collapsed_matches[-1][1] = matches[index][1]
    else:
      collapsed_matches.append(matches[index])
  underscores = [item for sublist in collapsed_matches for item in sublist]
  underscore_i = 0
  result = []
  for i in range(len(string)):
    if underscore_i < len(underscores) and underscores[underscore_i] == i:
      result.append(f'_{string[i]}')
      underscore_i += 1
    else:
      result.append(string[i])
  if underscore_i == len(underscores) - 1:
    result.append('_')
  return ''.join(result)
