import random
import re
from parse import *
from naivebayesproj import *
from hmm import *

inp1 = raw_input("Enter your input here:").split()
inp = [x.lower() for x in inp1]

poswords = open("poswords.txt").readlines()

negwords = open("negwords.txt").readlines()

questionwords = ["What", "Why", "Where", "When", "How", "Who", "Is", "Are", 
				"what", "why", "where", "when", "how", "who", "is", "are"]

greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
				"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up"]

farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn", 
				"goodbye", "later", "ok"]

# Seed Word List Generator
pos_seeds = [word for word in poswords if word in list(c.dict.keys())]
neg_seeds = [word for word in negwords if word in list(c.dict.keys())]
greet_seeds = [word for word in greetingwords if word in list(c.dict.keys())]
farewell_seeds = [word for word in farewellwords if word in list(c.dict.keys())]
other_seeds = [word for word in commonwords if word in list(c.dict.keys())]


def classifyInput():
	if inp[0] in questionwords:
		# find longest two words in the question to seed
		sortedwords = sorted(inp, key=len).reverse()
		# return chat output from longest two words
		return chat(sortedwords[0], sortedwords[1])
	else:
		beliefindex = toBelief(inp) # returns index of belief state given input
		# pick random word in the bucket of seed words
		if beliefindex == 0:
			seed = random.choice(pos_seeds)
		if beliefindex == 1:
			seed = random.choice(neg_seeds)
		if beliefindex == 2:
			seed = random.choice(greet_seeds)
		if beliefindex == 3:
			seed = random.choice(farewell_seeds)
		if beliefindex == 4:
			seed = random.choice(other_seeds)

	second_seed = random.choice(words2[seed])
	chat(seed, second_seed)
	


def chat(w1, w2):
	output_string = ""
	output_string += w1 + " " + w2
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

classifyInput()
