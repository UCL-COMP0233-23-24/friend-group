class Person:
    """A class to represent an individual and their connections."""

    def __init__(self, name, age, job):
        """Create a new Person with the given name, age, and job and no connections."""
        self.name = name
        self.age = age
        self.job = job
        self.connections = dict()

    def add_connection(self, person, relation):
        """Add a new connection to a person"""
        if person in self.connections:
            raise ValueError(f"I already know about {person.name}")
        self.connections[person] = relation

    def forget(self, person):
        """Removes any connections to a person"""
        if person in self.connections:
            del self.connections[person]

def average_age(group):
    """Compute the average age of the group's members."""
    all_ages = [person.age for person in group]
    return sum(all_ages) / len(group)

if __name__ == "__main__":
    # Create the group members one by one
    jill = Person("Jill", 26, "biologist")
    zalika = Person("Zalika", 28, "engineer")
    john = Person("John", 27, "teacher")
    nash = Person("Nash", 34, "doctor")

    # Add the connections one by one
    jill.add_connection(zalika, "friend")
    jill.add_connection(john, "colleague")
    jill.add_connection(nash, "family")
    nash.add_connection(jill, "family")

    # Forget Nash and John's connection
    nash.forget(john)

    # Then create the group
    my_group = {jill, zalika, john, nash}

    assert len(my_group) == 4, "Group should have 4 members"
    assert average_age(my_group) == 28.75, "Average age of the group is incorrect!"
    assert len(nash.connections) == 1, "Nash should only have one relation"
    print("All assertions have passed!")
