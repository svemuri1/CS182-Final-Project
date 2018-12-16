import re
import numpy as np
import util

commonword = open("20k.txt").readlines()
commonwords = map(str.strip, commonword)

# # Parses messages
	# infile = "ksmsg1.txt"
	# outfile = "svmsg1.txt"
	# f_read = open(infile, "r")
	# f_write = open(outfile, "a")
	# name = "Sid"
	# write = False
	# for line in f_read:
	# 	if write == True:
	# 		f_write.write(line)
	# 		write = False
	# 	if re.match(name, line) != None:
	# 		write = True
	# f_write.close()
	# f_read.close()

# Create transition probability matrix
# indices: greetings = 0, pos = 1, neg = 2, farewell = 3

class DictBuilder:

	def __init__(self, index=0):
		self.words = {}
		self.words2 = {}

	def ord2(self,outfile):
		# Create dictionary of order-2 for markov chain
		f = open(outfile, "r")
		for line in f:
			lst = line.rstrip("\n").split(" ")
			for i in range(len(lst)-2):
				key = (lst[i], lst[i+1])
				value = lst[i+2]
				if key in self.words:
					self.words[key].append(value)
				else:
					self.words[key] = [value]
		f.close()
		# print len(self.words)

		# Create dictionary of order-1 mappings
		f = open(outfile, "r")
		for line in f:
			lst = line.rstrip("\n").split(" ")
			for i in range(len(lst)-1):
				key = lst[i]
				value = lst[i+1]
				if key in self.words2:
					self.words2[key].append(value)
				else:
					self.words2[key] = [value]
		f.close()

		self.transitions = np.ones([5,5])
		poswords1 = open("poswords.txt").readlines()
		poswords = map(str.strip, poswords1)
		negwords1 = open("negwords.txt").readlines()
		negwords = map(str.strip, negwords1)
		greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
						"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up"]

		farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn",
						"goodbye", "later", "ok"]

		# Seed Word List Generator
		pos_seeds = [word for word in commonwords if word in poswords]
		neg_seeds = [word for word in commonwords if word in negwords]
		greet_seeds = [word for word in commonwords if word in greetingwords]
		farewell_seeds = [word for word in commonwords if word in farewellwords]

		# Create Transition Probabilities
		totalCount = 0
		for key in self.words2:
			if key in greetingwords:
				for value in self.words2[key]:
					if value  in greetingwords:
						self.transitions[0][0] += 1
					elif value in poswords:
						self.transitions[1][0] += 1
					elif value in negwords:
						self.transitions[2][0] += 1
					elif value in farewellwords:
						self.transitions[3][0] += 1
					else:
						self.transitions[4][0] += 1
			elif key in poswords:
				for value in self.words2[key]:
					if value in greetingwords:
						self.transitions[0][1] += 1
					elif value in poswords:
						self.transitions[1][1] += 1
					elif value in negwords:
						self.transitions[2][1] += 1
					elif value in farewellwords:
						self.transitions[3][1] += 1
					else:
						self.transitions[4][1] += 1
			elif key in negwords:
				for value in self.words2[key]:
					if value in greetingwords:
						self.transitions[0][2] += 1
					elif value in poswords:
						self.transitions[1][2] += 1
					elif value in negwords:
						self.transitions[2][2] += 1
					elif value in farewellwords:
						self.transitions[3][2] += 1
					else:
						self.transitions[4][2] += 1
			elif key in farewellwords:
				for value in self.words2[key]:
					if value in greetingwords:
						self.transitions[0][3] += 1
					elif value in poswords:
						self.transitions[1][3] += 1
					elif value in negwords:
						self.transitions[2][3] += 1
					elif value in farewellwords:
						self.transitions[3][3] += 1
					else:
						self.transitions[4][3] += 1
			else:
				for value in self.words2[key]:
					if value in greetingwords:
						self.transitions[0][4] += 1
					elif value in poswords:
						self.transitions[1][4] += 1
					elif value in negwords:
						self.transitions[2][4] += 1
					elif value in farewellwords:
						self.transitions[3][4] += 1
					else:
						self.transitions[4][4] += 1

		for i in range(5):
			rowSum = 0
			for j in range(5):
				rowSum += self.transitions[i][j]
			for j in range(5):
				if (rowSum != 0):
					self.transitions[i][j] = self.transitions[i][j]/float(rowSum)

		# build dictionary of words and index values to map to emission table
		self.wordmapping = util.Counter()
		for i, word in enumerate(commonwords):
			self.wordmapping[word] = i

		# Build emission probability table
		self.emissions = np.ones([5,20000])
		for j in range(20000):
			if commonwords[j] in greetingwords:
				self.emissions[0][j] += 10
			elif commonwords[j] in poswords:
				self.emissions[1][j] += 10
			elif commonwords[j] in negwords:
				self.emissions[2][j] += 10
			elif commonwords[j] in farewellwords:
				self.emissions[3][j] += 10
			else:
				self.emissions[4][j] += 10

		# print(np.sum(emissions))
		for i in range(5):
			rowSum = 0
			for j in range(20000):
				rowSum += self.emissions[i][j]
			for j in range(20000):
				if (rowSum != 0):
					self.emissions[i][j] = self.emissions[i][j]/float(rowSum)


n = DictBuilder()
n.ord2("ksmsg1.txt")
n.ord2("ksmsg2.txt")
n.ord2("ksmsg3.txt")
n.ord2("svmsg1.txt")
n.ord2("svmsg2.txt")
n.ord2("svmsg3.txt")
n.ord2("svmsg4.txt")
n.ord2("smmsg1.txt")
n.ord2("smmsg2.txt")

