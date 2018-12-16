transition_table = [[0.33]*3, [0.33]*3, [0.33]*3]
evidence_prob = [{'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}]
name = {'Kevin':0, 'Sreya':1, 'Sid':2}
state_space = [name[key] for key in name.keys()]

from parse import *

evidence_sequence = [wordmapping[word] for word in evidence]

# Save the results from the current iteration

# buiid on next iteration

# compute belief state for state candidate: forward algorithm
# def computeHighestBeliefState(state, evidence_sequence):
#     # calculate P(e_t | x_t)
#     evidence_prob = emission_table[state][evidence_sequence[len(evidence_sequence)-1]]
#     # calculate sum of joint probabilities of previous states:
#     transition_weight = 0.0
#     for x in state_space:
#         # add probabilities of observing e_{1:t} and x_t from every prev. state
#         transition_weight += emission_table[x][evidence_sequence[len(evidence_sequence)-2]] \
#                             * transition_table[x][state]
#     return evidence_prob * transition_weight

# forward algorithm... using DP!
def computeHighestBeliefState(state, evidence_sequence):
    transition_table = np.zeros([5, len(evidence_sequence) + 1])
    for i in range(transition_table.shape[0]):
        transition_table[i][0] = 0.20
    for j in range(transition_table.shape[1], 1):
        for i in range(transition_table.shape[0]):
            evidence_prob = emission_table[i][evidence_sequence[j - 1]]
            to_state_prob = 0.0
            for prev in range(transition_table.shape[0]):
                to_state_prob += state_transitions[i][prev] * transition_table[prev][j-1]
            transition_table[i][j] = evidence_prob * to_state_prob
    return [transition_table[x][transition_table.shape[1] - 1] for x in range(transition_table.shape[0])]


def currentBeliefState(state, evidence_sequence):
    state_probs = computeHighestBeliefState(state, evidence_sequence)
    return state_probs.index(max(state_probs))


import re

def removeFluff(strLst):
    lst = []
    for s in strLst:
        s = (s.replace("?", "")).replace(" ", "").replace(".", "").replace("!", "")
        lst.append(s)
    is_fluff = lambda x: x not in ["the", 'hmm', 'like', 'a', 'well', '...']
    lst = filter(is_fluff, lst)
    return lst



# Note: Baum - Welch Algorithm For Determining Matrix Weights
