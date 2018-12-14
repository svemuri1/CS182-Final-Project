import re

# Parses messages
infile = "svmsg4.txt"
outfile = "outfile.txt"
f_read = open(infile, "r")
f_write = open(outfile, "a")
name = "Sreya"
write = False
for line in f_read:
	if write == True:
		f_write.write(line)
		write = False
	if re.match(name, line) != None:
		write = True
f_write.close()
f_read.close()

# Create dictionary for markov chain
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