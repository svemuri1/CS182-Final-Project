import pickle as p

def save_obj(obj, name): # from stackoverflow
    with open('time_test/'+ name + '.pkl', 'wb') as f:
        p.dump(obj, f, p.HIGHEST_PROTOCOL)

def load_obj(name): # from stackoverflow
    with open('time_test/' + name + '.pkl', 'rb') as f:
        return p.load(f)

trial_number = 10

msg_lst = ['./ksmsg/ksmsg{0}.txt'.format(x+1) for x in range(trial_number)] + \
          ['./svmsg/svmsg{0}.txt'.format(x+1) for x in range(trial_number)] + \
          ['././smmsg/smmsg{0}.txt'.format(x+1) for x in range(trial_number)]
