# Naive Bayes Implementation with FB Data
from math import log
from save import *

class TextClassifier:

	def __init__(self, index=0):
		self.dict = {"Sreya": 0}
		self.names = ["Kevin", "Sreya", "Sidharth"]
		self.counts = [[0] * 50000 for _ in range(3)]

	def q4(self, infile):
	        """
	        You'll notice that actual words didn't appear in the last question.
	        Array indices are nicer to work with than words, so we typically
	        write a dictionary encoding the words as numbers. This turns
	        review strings into lists of integers. You will count the occurrences
	        of each integer in reviews of each class.

	        The infile has one review per line, starting with the rating and then a space.
	        Note that the "words" include things like punctuation and numbers. Don't worry
	        about this distinction for now; any string that occurs between spaces is a word.

	        You must do three things in this question: build the dictionary,
	        count the occurrences of each word in each rating and count the number
	        of reviews with each rating.
	        The words should be numbered sequentially in the order they first appear.
	        counts[ranking][word] is the number of times word appears in any of the
	        reviews corresponding to ranking
	        nrated[ranking] is the total number of reviews with each ranking

	        Hint: Make sure to actually set the self.dict, self.counts, and
	        self.nrated variables!
	        """
	        # self.dict = {"compsci": 0, "182": 1, ".": 2}
	        # self.counts = {0: [0,0,0],1: [0,0,0],2: [1,1,1],3: [0,0,0],4: [0,0,0]}
	        # self.nnames = {"Kevin Stephen": self.dict, "Sreya Vemuri" : 0, "Sid Menon" : 0}
	        # self.nrated = [0,0,1,0,0]

	        # Loop through file and fill dict and nrated

	        self.nnames = {"Kevin Stephen": 0, "Sreya Vemuri" : 0, "Sid Menon" : 0}
	        self.realnames = {0: "Kevin Stephen", 1: "Sreya Vemuri", 2: "Sid Menon"}
	        self.months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"}


	        f = open(infile, 'r')

	        linecount = 0

	        for line in f:
	        	linecount += 1
	        	lst = line.rstrip("\n").split(" ")
	        	if len(lst) > 1:
		            if not (lst[0] + " " + lst[1]) in self.names and lst[0] not in self.months:
			            for word in lst:
			                if word not in self.dict.keys():
			                    self.dict[word] = len(self.dict)
					elif (lst[0] + " " + lst[1]) in self.names:
						self.nnames[lst[0] + " " + lst[1]] += 1
	        f.close()

	def q45(self, infile):

	        f = open(infile, 'r')

	        l = 0

	        switch = 1
	        for line in f:
	        	lst = line.rstrip("\n").split(" ")
	        	if lst[0] == "Kevin":
	        		l = 0
	        	if lst[0] == "Sreya":
	        		l = 1
	        	if lst[0] == "Sidharth":
	        		l = 2

	        	if len(lst) > 1:
	        		if switch == 1 and lst[0] not in self.months:
	        			switch = 0
	        			for word in lst:
	        				encoding = self.dict[word]
			                self.counts[l][encoding] += 1
	        		if lst[0] in self.names:
	        			switch = 1
		        	# if lst[0] not in self.months and (lst[0] + " " + lst[1]) not in self.names:
	        f.close()

	def q5(self, alpha=1):
	        """
	        Now you'll fit the model. For historical reasons, we'll call it F.
	        F[rating][word] is -log(p(word|rating)).
	        The ratings run from 0-4 to match array indexing.
	        Alpha is the per-word "strength" of the prior (as in q2).
	        (What might "fairness" mean here?)

	        Hint: p(word|rating) =
	        (alpha + self.counts[rating][word]) /
	          (sum(self.counts[rating]) + (alpha * len(self.counts[rating])))

	        Though, you might need to add some float() operators.
	        """
	        self.F = [[0] * len(self.dict) for _ in range(3)]

	        curr = 0
	        for name in range(len(self.F)):
	            for word in range(len(self.dict)):
	                prob = float(alpha + self.counts[name][word]) / float((sum(self.counts[name]) + (alpha * len(self.counts[name]))))
	                self.F[name][word] = -1 * log(prob)

	def q6(self, infile):
	        """
	        Test time! The infile has the same format as it did before. For each review,
	        predict the rating. Ignore words that don't appear in your dictionary.
	        Are there any factors that won't affect your prediction?
	        You'll report both the list of predicted ratings in order and the accuracy.
	        """
	        count = 0
	        accuracy = 0
	        predictions = []

	        inputwords = infile

	        totals =[0,0,0]

	        for word in inputwords:
	            if word in self.dict.keys():
	                encoded = self.dict[word]
	                for name in range(0,3):
	                    totals[name] += self.F[name][encoded]
	        our_rating = totals.index(min(totals))

		return self.realnames[our_rating]
	        # return [predictions, float(accuracy)/count]

	def q7(self, infile):
	        """
	        Alpha (q5) is a hyperparameter of this model - a tunable option that affects
	        the values that appear in F. Let's tune it!
	        We've split the dataset into 3 parts: the training set you use to fit the model
	        the validation and test sets you use to evaluate the model. The training set
	        is used to optimize the regular parameters, and the validation set is used to
	        optimize the hyperparameters. (Why don't you want to set the hyperparameters
	        using the test set accuracy?)
	        Find and return a good value of alpha (hint: you will want to call q5 and q6).
	        What happens when alpha = 0?
	        """
		return 0.1


def createClassifier():
	c = TextClassifier()
	print "Creating Identifier: Processing training set..."
	for msg in msg_lst:
		c.q4(msg)
	print "Fitting model..."
	for msg in msg_lst:
		c.q45(msg)
	c.q5()
	return c
