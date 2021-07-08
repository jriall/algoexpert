# Verifying an Alien Dictionary

# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    alien_dictionary = {}
    for index, char in enumerate(order):
      alien_dictionary[char] = index
    for i in range(len(words) - 1):
      are_words_sorted = self.are_words_sorted(words[i], words[i + 1], alien_dictionary)
      if not are_words_sorted:
        return False
    return True
  
  def are_words_sorted(self, word1: str, word2: str, alien_dictionary: dict) -> bool:
    j = 0
    while True:
      if len(word1) <= j and len(word2) <= j or len(word1) <= j:
        return True
      elif len(word2) <= j:
        return False
      letter1_value = alien_dictionary[word1[j]]
      letter2_value = alien_dictionary[word2[j]]
      if letter1_value == letter2_value:
        j += 1
      elif letter1_value < letter2_value:
        return True
      else:
        return False  
