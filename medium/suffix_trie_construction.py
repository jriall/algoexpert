# Suffix Trie Construction
# Write a SuffixTrie class for a Suffix-Trie-like data structure. The class
# should have a root property set to be the root node of the trie and should
# support:

# Creating the trie from a string; this will be done by calling the
# populateSuffixTrieFrom method upon class instantiation, which should populate
# the root of the class.
# Searching for strings in the trie.
# Note that every string added to the trie should end with the special endSymbol
# character: "*".

# Sample Input (for creation)
# string = "babc"
# Sample Output (for creation)
# The structure below is the root of the trie.
# {
#   "c": {"*": true},
#   "b": {
#     "c": {"*": true},
#     "a": {"b": {"c": {"*": true}}},
#   },
#   "a": {"b": {"c": {"*": true}}},
# }
# Sample Input (for searching in the suffix trie above)
# string = "abc"

# Solution

class SuffixTrie:
  def __init__(self, string):
    self.root = {}
    self.endSymbol = "*"
    self.populateSuffixTrieFrom(string)

  def populateSuffixTrieFrom(self, string):
    startIndex = 0
    while startIndex < len(string):
      curr = self.root
      for index in range(startIndex, len(string)):
        letter = string[index]
        if letter in curr:
          curr = curr[letter]
        else:
          curr[letter] = {}
          curr = curr[letter]
        if index == len(string) - 1:
          curr[self.endSymbol] = True
      startIndex += 1

  def contains(self, string):
    curr = self.root
    for char in string:
      if char in curr:
        curr = curr[char]
      else:
        return False
    return self.endSymbol in curr
