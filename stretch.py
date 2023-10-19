def init_friend(name:str, age=None, job=None):
    my_group[name] = {
        "age" : age,
        "job" : job,
        "connections" : {},
    }

def init_connection(host:str, party:str, descriptor:str="friend"):
    if party not in my_group:
        init_friend(party)
    my_group[host]["connections"][party] = descriptor

def forget_connection(host:str, party:str):
        my_group[host]["connections"].pop(party)

def average_age():
    cum_age = 0
    n=0
    for name in my_group:
        try:
            cum_age+=my_group[name]["age"]
            n+=1
        except:
            pass
    return cum_age/n