import pickle as p

def save_obj(obj, name): # from stackoverflow
    with open('time_test/'+ name + '.pkl', 'wb') as f:
        p.dump(obj, f, p.HIGHEST_PROTOCOL)

def load_obj(name): # from stackoverflow
    with open('time_test/' + name + '.pkl', 'rb') as f:
        return p.load(f)

msg_lst = ['ksmsg{0}.txt'.format(x+1) for x in range(10)] + \
          ['svmsg{0}.txt'.format(x+1) for x in range(10)] + \
          ['smmsg{0}.txt'.format(x+1) for x in range(10)]
