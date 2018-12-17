import random
import re
from parse import *
from naivebayesproj import *
from hmm import *

userwords = []

poswords1 = open("poswords.txt").readlines()
poswords0 = map(str.strip, poswords1)
poswords = [x.lower() for x in poswords0]

negwords1 = open("negwords.txt").readlines()
negwords0 = map(str.strip, negwords1)
negwords = [x.lower() for x in negwords0]

questionwords = ["What", "Why", "Where", "When", "How", "Who", "Is", "Are", 
				"what", "why", "where", "when", "how", "who", "is", "are"]

greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
				"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up"]

farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn", 
				"goodbye", "later", "ok"]

# Seed Word List Generator
pos_seeds = [word for word in poswords if word in list(n.words2.keys())]
neg_seeds = [word for word in negwords if word in list(n.words2.keys())]
greet_seeds = [word for word in greetingwords if word in list(n.words2.keys())]
farewell_seeds = [word for word in farewellwords if word in list(n.words2.keys())]
other_seeds = [word for word in commonwords if word in list(n.words2.keys())]


def classifyInput(inp):
	if len(inp) == 0:
		print "Please enter a longer question:"
		return 1
	if inp[0] in questionwords:
		# find longest two words in the question to seed
		inp.sort(key=len,reverse=True)
		# return chat output from longest two words
		if len(inp) > 1:
			if inp[0] in other_seeds and inp[1] in other_seeds:
				return chat(inp[0], inp[1])
			else:
				seed = random.choice(other_seeds)
				second_seed = random.choice(n.words2[seed])
				return chat(seed, second_seed)
		else:
			print "Please enter a longer question:"
			return 1
	else:
		beliefindex = toBelief(inp) # returns index of belief state given input
		# pick random word in the bucket of seed words
		if beliefindex == 0:
			seed = random.choice(greet_seeds)
		if beliefindex == 1:
			seed = random.choice(pos_seeds)
		if beliefindex == 2:
			seed = random.choice(neg_seeds)
		if beliefindex == 3:
			seed = random.choice(farewell_seeds)
		if beliefindex == 4:
			seed = random.choice(other_seeds)
	second_seed = random.choice(n.words2[seed])
	return chat(seed, second_seed)

def chat(w1, w2):
	output_string = ""
	output_string += w1 + " " + w2
	words = n.words
	user1 = w1
	user2 = w2
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


for i in range(10):
	inp1 = raw_input("Enter your input here:").split()
	inp = [x.lower() for x in inp1]
	userwords.append(inp)
	classifyInput(inp)

print "Based on your responses, you're probably ", c.q6(userwords)
