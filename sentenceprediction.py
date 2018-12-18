import random
import re
import optparse
from save import *
from hmm import *
from parse import *
from naivebayesproj import *
import time

userwords = []
pos_seeds = []
neg_seeds = []
greet_seeds = []
farewell_seeds = []
other_seeds = []
questionwords = []
farewellwords = []
greetingwords = []

words = []
words2 = []

def load(n):
	global pos_seeds
	global neg_seeds
	global greet_seeds
	global farewell_seeds
	global other_seeds
	global words2
	global words
	poswords1 = open("poswords.txt").readlines()
	poswords0 = map(str.strip, poswords1)
	poswords = [x.lower() for x in poswords0]

	negwords1 = open("negwords.txt").readlines()
	negwords0 = map(str.strip, negwords1)
	negwords = [x.lower() for x in negwords0]

	questionwords = ["What", "Why", "Where", "When", "How", "Who", "Is", "Are",
					"what", "why", "where", "when", "how", "who", "is", "are"]

	greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
					"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up", "pleased", "meet"]

	farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn",
					"goodbye", "later", "ok"]

	# Seed Word List Generator
	pos_seeds = [word for word in poswords if word in list(n.words2.keys())]
	neg_seeds = [word for word in negwords if word in list(n.words2.keys())]
	greet_seeds = [word for word in greetingwords if word in list(n.words2.keys())]
	farewell_seeds = [word for word in farewellwords if word in list(n.words2.keys())]
	other_seeds = [word for word in n.commonwords if word in list(n.words2.keys())]
	words2 = n.words2
	words = n.words


def classifyInput(inp, wordmapping, emissions, transitions):

	questionwords = ["What", "Why", "Where", "When", "How", "Who", "Is", "Are",
					"what", "why", "where", "when", "how", "who", "is", "are"]

	if len(inp) == 0:
		print "Please enter a longer question:"
		return 1
	if inp[0] in questionwords:
		# find longest two words in the question to seed
		print "This is a question!"
		inp.sort(key=len,reverse=True)
		# return chat output from longest two words
		if len(inp) > 1:
			if inp[0] in other_seeds:
				second_seed = random.choice(words2[inp[0]])
				return chat(inp[0], second_seed)
			else:
				seed = random.choice(other_seeds)
				second_seed = random.choice(words2[seed])
				return chat(seed, second_seed)
		else:
			print "Please enter a longer question:"
			return 1
	else:
		# returns index of belief state given input
		beliefindex = toBelief(inp, wordmapping, transitions, emissions)
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
	second_seed = random.choice(words2[seed])
	return chat(seed, second_seed)

def chat(w1, w2):
	output_string = ""
	output_string += w1 + " " + w2
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


def parseOptions():
	optParser = optparse.OptionParser()
	optParser.add_option('-r', '--retrain',action='store_true', \
						dest='retrain', default=False, \
						help='Retrain Model (default %default)')
	opts, args = optParser.parse_args()
	if opts.retrain:
		print '### Retraining Model! Please Be Patient.... (-r) ###'
	else:
		print '### Using Pretrained Model! (No -r flag provided) ###'
	return opts



if __name__ == '__main__':

	opts = parseOptions()

	start = time.time()
	if opts.retrain: # if given -r , retrain markov model
		n = createDict()
		load(n)
		assert(len(other_seeds) > 0)
		save_obj(pos_seeds, 'pos_seeds')
		save_obj(neg_seeds, 'neg_seeds')
		save_obj(greet_seeds, 'greet_seeds')
		save_obj(farewell_seeds, 'farewell_seeds')
		save_obj(other_seeds, 'other_seeds')
		save_obj(questionwords, 'questionwords')
		save_obj(words, 'words')
		save_obj(words2, 'words2')
		emissions = n.emissions
		transitions = n.transitions
		wordmapping = n.wordmapping
		c = createClassifier()
		save_obj(c, 'classifier')
	else: # otherwise, just use old model
		pos_seeds = load_obj('pos_seeds')
		neg_seeds = load_obj('neg_seeds')
		greet_seeds = load_obj('greet_seeds')
		farewell_seeds = load_obj('farewell_seeds')
		other_seeds = load_obj('other_seeds')
		emissions = load_obj('emissions')
		transitions = load_obj('transitions')
		wordmapping = load_obj('wordmapping')
		words = load_obj('words')
		words2 = load_obj('words2')
		c = load_obj('classifier')

	print '### Text Bot Ready. Training Took {0} seconds ###'.format(time.time() - start)

	for i in range(10):
		inp1 = raw_input("Enter your input here:").split()
		inp = [x.lower() for x in inp1]
		for x in inp:
			userwords.append(x)
		classifyInput(inp, wordmapping, emissions, transitions)

	print "Based on your responses, you're probably", c.q6(userwords)
