# Group Anagrams
# Write a function that takes in an array of strings and groups anagrams
# together.

# Anagrams are strings made up of exactly the same letters, where order doesn't
# matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and
# "ofo" are anagrams.

# Your function should return a list of anagram groups in no particular order.

# Sample Input
# words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# Sample Output
# [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

# Solution

def group_anagrams(words):
	results = {}
	for word in words:
		alphabetized_string = ''.join(sorted(word))
		if alphabetized_string in results:
			results[alphabetized_string].append(word)
		else:
			results[alphabetized_string] = [word]
	return list(results.values())
