transition_table = [[0.33]*3, [0.33]*3, [0.33]*3]
evidence_prob = [{'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}, {'fun':0.1, 'cool':0.9}]
name = {'Sreya':0, 'Kevin':1, 'Sid':2}
state_space = [name[key] for key in name.keys()]

# compute belief state for state candidate
def computeHighestBeliefState(state, evidence_sequence):
    # calculate P(e_t | x_t)
    evidence_prob = emission_table[state][evidence_sequence[len(evidence_sequence)-1]]
    # calculate sum of joint probabilities of previous states:
    transition_weight = 0.0
    for x in state_space:
        # add probabilities of observing e_{1:t} and x_t from every prev. state
        transition_weight += emission_table[x][evidence_sequence[len(evidence_sequence)-2]] \
                            * transition_table[x][state]
    return evidence_prob * transition_weight

def currentBeliefState(evidence_sequence):
    highest_belief = float('-inf')
    speaker = 0
    for x in state_space:
        belief_res = computeHighestBeliefState(x, evidence_sequence)
        if (belief_res > highest_belief):
            speaker = x
            highest_belief = belief_res 
    return speaker
