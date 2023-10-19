"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class person : 
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

Jill = person('Jill', 26, 'Biologist')
Zalika = person('Zalika', 28, 'Artist')
John = person('John', 27, 'Writer')
Nash = person('Nash', 34, 'Chef')



print(Jill.name)

#my_group = 
