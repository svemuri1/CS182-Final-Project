import random
from parse import *

# Given two words, predict sequence of words
key = random.choice(list(words))
output_string = ""
output_string += key[0] + " " + key[1]
(user1, user2) = key
while key in words:
	length = len(words[key])-1
	index = random.randint(0, length)
	output = words[key][index]
	output_string += " " + output
	user1 = user2
	user2 = output
	key = (user1, user2)
print output_string


