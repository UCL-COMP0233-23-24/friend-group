"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person:
    def __init__(self, name, age, job = ""):
        self.name = name
        self.age = age
        self.job = job
        self.connection = {}

    def addConnection(self, person, relation):
        self.connection[relation] = person

        if relation in ['friend', 'partner', 'cousin', 'sibling']:
            person.connection[relation] = self

    def listConnections(self):
        for key, value in self.connection.items():
            print(f"{value.name} is {self.name}'s {key}")


Jill = Person('Jill', 26, 'Biologist')
Zalika = Person('Zalika', 28, 'Artist')
John = Person('John', 27, 'Writer')
Nash = Person('Nash', 34, 'Chef')

Jill.addConnection(Zalika, 'friend')
Jill.addConnection(John, 'partner')
Nash.addConnection(John, 'cousin')
Nash.addConnection(Zalika, 'tenant')
Zalika.addConnection(Nash, 'landlord')

myGroup = [Jill, Zalika, John, Nash]


for person in myGroup:
    person.listConnections()

