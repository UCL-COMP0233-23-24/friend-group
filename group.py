"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class person : 
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.relations = []
    
    def add_relation(self, name, relation):
        self.relations.append({name:relation})


Jill = person('Jill', 26, 'Biologist')
Jill.add_relation('Zalika','friend')
Jill.add_relation('John','partner')

Zalika = person('Zalika', 28, 'Artist')
Zalika.add_relation('Jill','friend')

John = person('John', 27, 'Writer')
John.add_relation('Jill','partner')

Nash = person('Nash', 34, 'Chef')
Nash.add_relation('John','cousin')
Nash.add_relation('Zalika','landlord')

