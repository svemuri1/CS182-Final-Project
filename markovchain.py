# Pseudocode

# Import file of my texts
# for each line in the file
# if line i - 1 is a name, then put line i into a list of messages from person name

def importdata(self, infile):
	
names = ["Kevin Stephen", "Sreya Vemuri", "Sid Menon"]
data = {"Kevin Stephen":[], "Sreya Vemuri":[], "Sid Menon":[]}

for f in fileset: 
	f = open(infile, 'r')
	        
	for i in f: 
		# lst = line.rstrip("\n").split(" ")
		if lines[i - 1] in names:
			data[lines[i-1]].append(lines[i])

	f.close()

# data[name] is now a list in which each element is a message that "name" sent




