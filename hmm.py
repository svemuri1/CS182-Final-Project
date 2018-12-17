transition_table = [[0.33]*3, [0.33]*3, [0.33]*3]
evidence_prob = [{'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}]
name = {'Kevin':0, 'Sreya':1, 'Sid':2}
state_space = [name[key] for key in name.keys()]

from parse import *

# transitions , emissions, wordmap



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
def computeHighestBeliefState(evidence_sequence):
    transition_table = np.zeros([5, len(evidence_sequence) + 1])
    for i in range(transition_table.shape[0]):
        transition_table[i][0] = 0.20
    for j in range(1, transition_table.shape[1]):
        for i in range(transition_table.shape[0]):
            evidence_prob = n.emissions[i][evidence_sequence[j - 1]]
            # print "{0} evidence of at {1} at timestep {2}".format(evidence_prob, i, j)
            to_state_prob = 0.0
            for prev in range(transition_table.shape[0]):
                to_state_prob += n.transitions[i][prev] * transition_table[prev][j-1]
            # print "{0} evidence of at {1} at timestep {2}".format(transition_table[i][j], i, j)
            transition_table[i][j] = evidence_prob * to_state_prob
            # print "{0} evidence of at {1} at timestep {2}".format(transition_table[i][j], i, j)
    return [transition_table[x][transition_table.shape[1] - 1] for x in range(transition_table.shape[0])]


def currentBeliefState(evidence_sequence):
    state_probs = computeHighestBeliefState(evidence_sequence)
    return state_probs.index(max(state_probs))


def toBelief(evidence_list):
    evidence_sequence = [n.wordmapping[word] for word in evidence_list]
    # print evidence_sequence
    return currentBeliefState(evidence_sequence)

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
