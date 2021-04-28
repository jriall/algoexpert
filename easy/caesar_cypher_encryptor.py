# Caesar Cipher Encryptor
# Given a non-empty string of lowercase letters and a non-negative integer
# representing a key, write a function that returns a new string obtained by
# shifting every letter in the input string by k positions in the alphabet,
# where k is the key.

# Note that letters should "wrap" around the alphabet; in other words, the
# letter z shifted by one returns the letter a.

def caesarCipherEncryptor(string, key):
  result = ''
	for letter in string:
		new_char_code = ord(letter) + key
		# Minus 97 (lowercase a), then modulo by the number of letters in the
		# alphabet to make anything above a-z wrap back around to a-z, then
		# finally add the 97 back to get the correcy character code.
		result += chr((new_char_code - 97) % 26 + 97)
	return result
