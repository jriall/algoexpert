# First Non-Repeating Character
# Write a function that takes in a string of lowercase English-alphabet letters
# and returns the index of the string's first non-repeating character.

# The first non-repeating character is the first character in a string that
# occurs only once.

# If the input string doesn't have any non-repeating characters, your function
# should return -1.

def first_non_repeating_character(string):
  counter = {}
  for character in string:
    if character in counter:
      counter[character] += 1
    else:
      counter[character] = 1
  for index, character in enumerate(string):
    if counter[character] == 1:
      return index
    return -1
