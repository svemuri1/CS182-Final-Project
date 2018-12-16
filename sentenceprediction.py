import random
import re
from parse import *

inp = raw_input("Enter your input here:").split()


poswords = open("poswords.txt").readlines()

print type(poswords)

negwords = open("negwords.txt").readlines()

questionwords = ["What", "Why", "Where", "When", "How", "Who", "Is", "Are", 
				"what", "why", "where", "when", "how", "who", "is", "are"]

greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
				"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up"]

farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn", 
				"goodbye", "later", "ok"]

if inp[0] in questionwords:
	# find longest two words in the question to seed
	sortedwords = sorted(inp, key=len).reverse()

	# return chat output from longest two words
	return chat(sortedwords[0], sortedwords[1])
else:

	# HMM to classify input
	




def chat(w1, w2):
	output_string = ""
	output_string += user1 + " " + user2
	# output_string += key[0] + " " + key[1]
	# user1 = key[0]
	# user2 = key[1]
	# (user1, user2) = key
	key = (w1, w2)
	while key in words:
		length = len(words[key])-1
		index = random.randint(0, length)
		output = words[key][index]
		output_string += " " + output
		user1 = user2
		user2 = output
		key = (user1, user2)
	print output_string

