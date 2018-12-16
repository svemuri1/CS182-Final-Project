import re
import numpy as np

commonword = open("20k.txt").readlines()
commonwords = map(str.strip, commonword)

# Parses messages
infile = "smmsg2.txt"
outfile = "smmsg1.txt"
f_read = open(infile, "r")
f_write = open(outfile, "a")
name = "Sid"
write = False
for line in f_read:
	if write == True:
		f_write.write(line)
		write = False
	if re.match(name, line) != None:
		write = True
f_write.close()
f_read.close()

# Create dictionary of order-2 for markov chain
words = {}
f = open(outfile, "r")
for line in f:
	lst = line.rstrip("\n").split(" ") 
	for i in range(len(lst)-2):
		key = (lst[i], lst[i+1])
		value = lst[i+2]
		if key in words:
			words[key].append(value)
		else:
			words[key] = [value]
f.close()

# Create dictionary of order-1 mappings
words2 = {}
f = open(outfile, "r")
for line in f:
	lst = line.rstrip("\n").split(" ")
	for i in range(len(lst)-1):
		key = lst[i]
		value = lst[i+1]
		if key in words2:
			words2[key].append(value)
		else:
			words2[key] = [value]
f.close()

# Create transition probability matrix
# indices: greetings = 0, pos = 1, neg = 2, farewell = 3
transitions = np.ones([4,4])
poswords1 = open("poswords.txt").readlines()
poswords = map(str.strip, poswords1)
negwords1 = open("negwords.txt").readlines()
negwords = map(str.strip, negwords1)
greetingwords = ["hello", "hi", "hey", "greetings", "evening", "morning", "afternoon", "up", "Pleased"
				"Hello", "Hi", "Hey", "Greetings", "Evening", "Morning", "Afternoon", "Up"]

farewellwords = ["Goodbye", "Seeya", "goodbye", "cya", "ttyl", "ttfn", "cu", "gtg", "bye", "goodnight", "gn", 
				"goodbye", "later", "ok"]

totalCount = 0
for key in words2:
	if key in greetingwords:
		for value in words2[key]:
			if value  in greetingwords:
				transitions[0][0] += 1
			elif value in poswords:
				transitions[0][1] += 1
			elif value in negwords:
				transitions[0][2] += 1
			elif value in farewellwords:
				transitions[0][3] += 1
	if key in poswords:
		for value in words2[key]:
			if value in greetingwords:
				transitions[1][0] += 1
			elif value in poswords:
				transitions[1][1] += 1
			elif value in negwords:
				transitions[1][2] += 1
			elif value in farewellwords:
				transitions[1][3] += 1
	if key in negwords:
		for value in words2[key]:
			if value in greetingwords:
				transitions[2][0] += 1
			elif value in poswords:
				transitions[2][1] += 1
			elif value in negwords:
				transitions[2][2] += 1
			elif value in farewellwords:
				transitions[2][3] += 1
	if key in farewellwords:
		for value in words2[key]:
			if value in greetingwords:
				transitions[3][0] += 1
			elif value in poswords:
				transitions[3][1] += 1
			elif value in negwords:
				transitions[3][2] += 1
			elif value in farewellwords:
				transitions[3][3] += 1

for i in range(4):
	rowSum = 0
	for j in range(4):
		rowSum += transitions[i][j]
	for j in range(4):
		if (rowSum != 0):
			transitions[i][j] = transitions[i][j]/float(rowSum)
# print transitions

# build dictionary of words and index values to map to emission table
wordmapping = {}
for i, word in enumerate(commonwords):
	wordmapping[word] = i

# Build emission probability table
emissions = np.ones([4,20000])
for j in range(20000):
	if commonwords[j] in greetingwords:
		emissions[0][j] += 10
	if commonwords[j] in poswords:
		emissions[1][j] += 10
	if commonwords[j] in negwords:
		emissions[2][j] += 10
	if commonwords[j] in farewellwords:
		emissions[3][j] += 10

print(np.sum(emissions))

for i in range(4):
	rowSum = 0
	for j in range(20000):
		rowSum += emissions[i][j]
	for j in range(20000):
		if (rowSum != 0):
			emissions[i][j] = emissions[i][j]/float(rowSum)

