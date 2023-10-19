"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
class Person:
    def __init__(self, name, age, job = "jobless person", relationship = "no one"):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = relationship

    def forget(person1, person2):
        person1.relationship = "no one"
        person2.relationship = "no one"

    def add_person(name, age, job, relationship):
        return Person(name, age, job, relationship)

    def average_age(group):
        total = 0
        for person in group:
            total += group[person].age
        return total/len(group)
    


my_group = {
    "Jiachen": Person("Jiachen", 23, "student", "classmate"),
    "Kehan": Person("Kehan", 23, "student", "classmate"),
    "Nobody": Person("Nobody", 233)
}

# print("{0} is {1}, a {2} and he is {3}'s {4}.".format(my_group["Jiachen"].name, my_group["Jiachen"].age, my_group["Jiachen"].job, my_group["Kehan"].name, my_group["Jiachen"].relationship))
# print("{0} is {1}, a {2} and he is {3}'s {4}.".format(my_group["Kehan"].name, my_group["Kehan"].age, my_group["Kehan"].job, my_group["Jiachen"].name, my_group["Kehan"].relationship))
# print("{0} is {1}, a {2} and he is {3}'s {4}.".format(my_group["Nobody"].name, my_group["Nobody"].age, my_group["Nobody"].job, my_group["Kehan"].name, my_group["Nobody"].relationship))

Person.forget(my_group["Jiachen"], my_group["Kehan"])
my_group["Newton"] = Person.add_person("Nowton", 33, "basketball player", "idel")
average_age = Person.average_age(my_group)
print(average_age)