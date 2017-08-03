# read in the file
fin = open('p059_cipher.txt')
# print(fin.readlines())
numbers = fin.readline().strip().split(',')
#print(numbers)

intnums = []
for num in numbers:
	intnums.append(int(num))

#print(intnums)

# triply nested for loops
import string
alpha = string.ascii_lowercase


''' highly inefficient, but shows different combinations
# password = []
passwords = []
for letter1 in alpha:
	for letter2 in alpha:
		for letter3 in alpha:
			passwords.append([letter1, letter2, letter3])
			# print(passwords)
'''



import itertools
# passwords = list(itertools.combinations_with_replacement(alpha, 3)) 
passwords = list(itertools.permutations(alpha,3)) # order matters, so password was ('g', 'o', 'd'), but this wouldn't be a solution if order was low to high
#passwords = list(itertools.product(alpha,alpha,alpha))

length = len(intnums)

import math

repititions = math.ceil(length / 3)



commonWords = 

for password in passwords:
	key = password * repititions
	translation = [chr(first ^ ord(second)) for first, second in zip(intnums,key)] # convert a string into an ordinal, 'a' as an ordinal is the 97th integer
	#print(translation)
	text = ''.join(translation)
	if 'the' in text and 'to' in text:
		print(text)

	counter = 0
	for word in commonWords:
		if word in text:
			counter += 1

	if counter > 24:
		print(text, password)



''' # helpful example of xor
e = (1,2,3,4,5,6)
k = (7,8,9,7,8)
list(zip(e,k)) # zip stops at the end of the plain text, so doesnt matter if 'e' is a little longer

[chr(first ^ second) for first, second in zip(e,k)]
'''




# math module (floor and ceiling)

# figure out how to make a sequence of possible keys

# maybe get a list of common words to check against...

# 