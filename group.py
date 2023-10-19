"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {

        "Jill" : 
            {"connection" :{
                "friend" : "Zalika", 
                "partner" : "John"
            },
            "age" : 26,
            "job" : "biologist"},

            
        "Zalika" : 
            {"connection" :{
                "friend" : "Jill"
            },
            "age" : 28,
            "job" : "artist"},


       "John" : 
            {"connection" :{ 
                "partner" : "Jill"
            },
            "age" : 27,
            "job" : "writer"},


        "Nash" : 
            {"connection" :{
                "cousin" : "John", 
                "landlord" : "Zalika"
            },
            "age" : 34,
            "job" : "chef"}    

    }



# a = {name: info['age'] for name, info in my_group.items()}

# print(a)

print(my_group)

def forget(person1, person2):
    for name, info in my_group.items():
        if name == person1:

            for key, value in info['connection'].items():
                if value == person2:
                    info['connection'].pop(key)
                    break

    for name, info in my_group.items():    
        if name == person2:

            for key, value in info['connection'].items():
                if value == person1:
                    info['connection'].pop(key)
                    break

forget('Jill', 'Zalika')

print(my_group)

def average_age():
    ages = {info['age'] for name, info in my_group.items()}
    sum = 0
    for age in ages:
        sum += age
        average = sum/ len(ages)
    return average