"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
class Person:
    def __init__(self, name, age, profession=None):
        self.name = name
        self.age = age
        self.profession = profession
        self.relationships = {}

    def add_relationship(self, person, relation_type):
        if person not in self.relationships:
            self.relationships[person] = []
        self.relationships[person].append(relation_type)
        

    def get_relationships(self):
        return self.relationships

    def __repr__(self):
        return f"{self.name} is {self.age}, {self.profession if self.profession else 'No Profession'}, and {list(self.relationships.keys())[0].name}"

jill = Person("Jill", 26, "biologist")
zalika = Person("Zalika", 28, "artist")
john = Person("John", 27, "writer")
nash = Person("Nash", 34, "chef")

jill.add_relationship(zalika, "friend")
jill.add_relationship(john, "partner")


print(jill)




my_group = {'Jill':{
    'occupation': 'biologist',
    'friend': 'Zalika',
    'partner':'John',
    'age':'26'
},
'Zalika':{
    'age': '28',
    'occupation': 'artist',
    'friend':'Jill',
    'landlord':'Nash'
},
'John':{
'age':'27',
'occupation': 'writer',
'partner':'Jill',
'relative': 'Nash'

},
'Nash':{
    'age':'34',
    'occupation':'chef',
    'relative':'John',
    'tenant': 'Zalika'
}



}
