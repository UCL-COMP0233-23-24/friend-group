"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
#dictionary = {name:name, age:age, job:job}

#jill={name:'Jill', age:26, job: 'biologist'}
#zalika={name:'Zalika', age: 28, job: 'artist'}
#john={name:'John', age: 27, job: 'writer'}
#nash={name: 'Nash', age:34, job:'chef'}


my_group = [{'name':'Jill', 'age':26, 'job': 'biologist','relationships':[{'relation': 'friend', 'to_person': 'Zalika'},
                 {'relation': 'partner', 'to_person': 'John'}]},
            {'name':'Zalika', 'age': 28, 'job': 'artist','relationships':{'relation': 'friend', 'to_person': 'Jill'}},
            {'name':'John', 'age': 27, 'job': 'writer', 'relationships':{'relation': 'partner', 'to_person': 'John'}},
            {'name': 'Nash', 'age':34, 'job':'chef','relationships':[{'relation': 'cousin', 'to_person': 'John'},
                 {'relation': 'landlord', 'to_person': 'Zalika'}]}]

# relationships = [{'person': 'Jill', 'relation': 'friend', 'to_person': 'Zalika'},
#                  {'person': 'Jill', 'relation': 'partner', 'to_person': 'John'},
#                  {'person': 'Zalika', 'relation': 'friend', 'to_person': 'Jill'},
#                  {'person': 'John', 'relation': 'partner', 'to_person': 'John'},
#                  {'person': 'Nash', 'relation': 'cousin', 'to_person': 'John'},
#                  {'person': 'Nash', 'relation': 'landlord', 'to_person': 'Zalika'}]