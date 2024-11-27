subs=[]

def add_subs(def_sub):
    subs.append(def_sub)

def broadcast(type_mes,who,addons=None):
    for sub in subs:
        sub(type_mes,who,addons)