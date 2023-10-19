"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill", "Zalika","John","Nash","Huangmou"}
Jill = {"age":26,"job": "biologist","friend":"Zalika","partner":"John"}
Zalika = {"age":28,"job": "artist","friend":"Jill"}
John = {"age":27,"job": "writer","partner":"Jill"}
Nash = {"age":34,"job": "chef","cousin":"John","Landlord":"Zalika"}
Huangmou = {"age":21}

name_of_people = Jill
index = "Landlord"

if index in name_of_people:
    print(name_of_people[index])
else:
    print(None)

