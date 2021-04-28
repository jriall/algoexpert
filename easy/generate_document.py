# Generate Document
# You're given a string of available characters and a string representing a
# document that you need to generate. Write a function that determines if you
# can generate the document using the available characters. If you can generate
# the document, your function should return true; otherwise, it should return
# false.

# You're only able to generate the document if the frequency of unique
# characters in the characters string is greater than or equal to the frequency
# of unique characters in the document string. For example, if you're given
# characters = "abcabc" and document = "aabbccc" you cannot generate the
# document because you're missing one c.

# The document that you need to create may contain any characters, including
# special characters, capital letters, numbers, and spaces.

# Note: you can always generate the empty string ("").

def generate_document(characters, document):
    unique_document_characters = {}
	for character in characters:
		if unique_document_characters.get(character):
			unique_document_characters[character] += 1
		else:
			unique_document_characters[character] = 1
	for character in document:
		if character not in unique_document_characters or unique_document_characters[character] <= 0:
			return False
		unique_document_characters[character] -= 1
	return True
