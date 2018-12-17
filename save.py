import pickle as p

def save_obj(obj, name): # from stackoverflow
    with open('dict_store/'+ name + '.pkl', 'wb') as f:
        p.dump(obj, f, p.HIGHEST_PROTOCOL)

def load_obj(name): # from stackoverflow
    with open('dict_store/' + name + '.pkl', 'rb') as f:
        return p.load(f)
