# Reverse Words In String
# Write a function that takes in a string of words separated by one or more
# whitespaces and returns a string that has these words in reverse order. For
# example, given the string "tim is great", your function should return
# "great is tim".

# For this problem, a word can contain special characters, punctuation, and
# numbers. The words in the string will be separated by one or more whitespaces,
# and the reversed string must contain the same whitespaces as the original
# string. For example, given the string "whitespaces    4" you would be expected
# to return "4    whitespaces".

# Note that you're not allowed to to use any built-in split or reverse
# methods/functions. However, you are allowed to use a built-in join
# method/function.

# Also note that the input string isn't guaranteed to always contain words.

Sample Input
string = "AlgoExpert is the best!"
Sample Output
"best! the is AlgoExpert"

# Solution iterating through the string backwards

def reverse_words_in_string(string):
  result = []
  word = []
  for index in reversed(range(len(string))):
    if string[index] != ' ':
      word.insert(0, string[index])
    else:
      if len(word) > 0:
        result.append(''.join(word))
        word = []

      result.append(' ')
  result.append(''.join(word))
  return ''.join(result)

# Simpler solution iterating through the string in order

def reverse_words_in_string(string):
  result = []
  word = []
  for letter in string:
    if letter == ' ':
      if len(word) > 0:
        result.insert(0, ''.join(word))
        word = []
      result.insert(0, ' ')
    else:
      word.append(letter)
  result.insert(0, ''.join(word))
  return ''.join(result)
