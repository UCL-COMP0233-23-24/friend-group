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

group.add_person("Alice", 30, "Engineer")
group.add_person("Bob", 25, "Teacher")
group.add_person("Charlie", 35, "Doctor")

group.connect_people("Alice", "Bob", "Friend")
group.connect_people("Alice", "Charlie", "Colleague")
group.connect_people("Bob", "Charlie", "Friend")

# Accessing attributes and connections
alice = group.people["Alice"]
print(f"{alice.name} is {alice.age} years old and works as an {alice.job}.")
print(f"{alice.name}'s connections: {alice.connections}")

# Output:
# Alice is 30 years old and works as an Engineer.
# Alice's connections: {'Friend': ['Bob'], 'Colleague': ['Charlie']}

