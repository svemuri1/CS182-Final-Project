import numpy as np
transition_table = [[0.33]*3, [0.33]*3, [0.33]*3]
evidence_prob = [{'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}]
name = {'Kevin':0, 'Sreya':1, 'Sid':2}
state_space = [name[key] for key in name.keys()]

# from parse import *

# transitions , emissions, wordmap



# Save the results from the current iteration

# buiid on next iteration

# compute belief state for state candidate: forward algorithm

# forward algorithm... using DP!
def computeHighestBeliefState(evidence_sequence, emissions, transitions):
    transition_table = np.zeros([5, len(evidence_sequence) + 1]) # 5 for number of possible states
    for i in range(transition_table.shape[0]):
        transition_table[i][0] = 0.20
    for j in range(1, transition_table.shape[1]):
        for i in range(transition_table.shape[0]):
            evidence_prob = emissions[i][evidence_sequence[j - 1]]
            to_state_prob = 0.0
            for prev in range(transition_table.shape[0]):
                to_state_prob += transitions[i][prev] * transition_table[prev][j-1]
            transition_table[i][j] = evidence_prob * to_state_prob
    return [transition_table[x][transition_table.shape[1] - 1] for x in range(transition_table.shape[0])]


def currentBeliefState(evidence_sequence, emissions, transitions):
    state_probs = computeHighestBeliefState(evidence_sequence, transitions, emissions)
    return state_probs.index(max(state_probs))


def toBelief(evidence_list, wordmapping, emissions, transitions):
    evidence_sequence = [wordmapping[word] for word in evidence_list]
    # print evidence_sequence
    return currentBeliefState(evidence_sequence, emissions, transitions)

import re



def removeFluff(strLst):
    lst = []
    for s in strLst:
        s = (s.replace("?", "")).replace(" ", "").replace(".", "").replace("!", "")
        lst.append(s)
    is_fluff = lambda x: x not in ["the", 'hmm', 'like', 'a', 'well', '...']
    lst = filter(is_fluff, lst)
    return lst

# print toBelief("hi hello how are you".split(" "))

# Note: Baum - Welch Algorithm For Determining Matrix Weights
