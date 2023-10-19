"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.connections = {}  # Dictionary to store connections

    def add_connection(self, relation, person):
        # Add a connection to another person with a given relation
        if relation not in self.connections:
            self.connections[relation] = []
        self.connections[relation].append(person)

class GroupOfAcquaintances:
    def __init__(self):
        self.people = {}  # Dictionary to store people

    def add_person(self, name, age, job=None):
        # Create a new person and add them to the group
        person = Person(name, age, job)
        self.people[name] = person

    def connect_people(self, person1, person2, relation):
        # Connect two people in the group with a given relation
        if person1 in self.people and person2 in self.people:
            self.people[person1].add_connection(relation, person2)
            self.people[person2].add_connection(relation, person1)

# Example usage:
group = GroupOfAcquaintances()

group.add_person("Jill", 26, " biologist")
group.add_person("Zalika", 28, "artist")
group.add_person("John", 27, "writer")
group.add_person("Nash", 34, "chef")


group.connect_people("Jill", "Zalika", "Friend")
group.connect_people("Jill", "John", "partner")
group.connect_people("Nash", "John", "cousin")
group.connect_people("Nash", "Zalika", "landlord")



