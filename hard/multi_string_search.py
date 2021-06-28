# Multi string search

# Write a function that takes in a big string and an array of small strings, all
# of which are smaller in length than the big string. The function should return
# an array of booleans, where each boolean represents whether the small string
# at that index in the array of small strings is contained in the big string.

# Note that you can't use language-built-in string-matching methods.

# Sample Input #1
# bigString = "this is a big string"
# smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
# Sample Output #1
# [true, false, true, true, false, true, false]
# Sample Input #2
# bigString = "abcdefghijklmnopqrstuvwxyz"
# smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]
# Sample Output #2
# [true, true, false, true, true, false]

# Solution

TRIE_END_SYMBOL = '*'

def multiStringSearch(bigString, smallStrings):
  trie = Trie()
  for string in smallStrings:
    trie.insert(string)
  results = {}
  for i in range(len(bigString)):
    curr = trie.results
    for j in range(i, len(bigString)):
      if bigString[j] not in curr:
        break
      else:
        curr = curr[bigString[j]]
      if TRIE_END_SYMBOL in curr:
        results[bigString[i:j + 1]] = True
  return [results.get(string, False) for string in smallStrings]


class Trie:
  results = {}
  
  def insert(self, string):
    curr = self.results
    for letter in string:
      if letter in curr:
        curr = curr[letter]
      else:
        curr[letter] = {}
        curr = curr[letter]
    curr[TRIE_END_SYMBOL] = True 
      