# TITLE: quad_vowels >> gen_quad_vowels.py
# AUTHOR: Chalmer Lowe
# DESCRIPTION:
# Read all the values from the file: words.txt.
# Each line contains a word.
# Each word has one or more vowels
# Deduplicate the words, so only a single copy remains
#     of any words that might have duplicates and count
#     all the words that have four OR more vowels.
#
# For example, if the following words were in the file:
#
# pathogen       > only 3 vowels
# preselecting   > 4 vowels
# spacefaring    > 4 vowels
# pathogen       # Duplicate and only 3 vowels
# adage          > only 3 vowels
# spacefaring    # Duplicate and 4 vowels

# Thus the total word count includes: preselecting, spacefaring
#     for a total of 2.

# ==============================================================
# Your code goes here:

from random import sample, shuffle
percent = 0.10
dupe_percent = 0.30

# count the vowels
def count_vowels(word):
	vowels = 'aeiou'

	''' optimize this code with list comprehension
	counter = 0
	for letter in word:
		if letter in vowels: # check if letter is a vowel
			counter += 1 # increment a counter
	'''

	''' also be able to return this through return
	counter = sum([1 for letter in word if letter in vowels]) # emulates the above for loop
	return counter
	'''

	return sum([1 for letter in word if letter in vowels]) # just return the sum rather than having a line of list comprehension



# open and read the file
with open('words.txt') as fin:
	# words = fin.read().split('\n') # if there is a newline character, split the full string into a list
	words = fin.readlines() # leave the new line characters, but these are not counted in vowels
	words = set(words) # deduplicate by converting the list into a set
	# print(len(words))
	total = 0
	vowels = 'aeiou'

	for word in words:
		''' emulate below and doesn't push a list into memory
		if count_vowels(word) >= 4:
			total += 1
		# print(word, count_vowels(word))
		'''

		if sum(    [1 for letter in word if letter in vowels]    ) >= 4:
			total += 1

	print(total)





