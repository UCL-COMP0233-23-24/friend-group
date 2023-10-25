"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group_1 = {"Name": "Jill",
            "Age": 26,
            "Jobs": "Biologist",
            "Relation": {"Zanika": "friend", "John": "partner"}}
print(my_group_1.values())

my_group_2 = {"Name": "Zanika",
              "Age": 28,
              "Jobs": "Artist",
              "Relation": {"Jill": "friend"}}
print(my_group_2.values())

my_group_3 = {"Name": "John",
              "Age": 27,
              "Jobs": "Writer",
              "Relation": {"Jill": "partner"}}
print(my_group_3.values())

my_group_4 = {"Name": "Nash",
            "Age": 34,
            "Jobs": "Chef",
            "Relation": {"John": "cousin", "Zanika": "landlord"}}
print(my_group_4.values())

#add an age list and find the max value
age_list = [26,27,28,34]
print(max(age_list))

#sum of all the total relations of each member of the group
total_relations = len(my_group_1["Relation"]) + len(my_group_2["Relation"]) + len(my_group_3["Relation"]) + len(my_group_4["Relation"])
print("total sum of relations: ", total_relations)

#divide the total relations by 4 (number of members)
average_relations = total_relations / 4
print("The average relations is: ", average_relations)

#create a list of group members
group_members = [my_group_1, my_group_2, my_group_3, my_group_4]

#print the max age for a person with at least 1 relation using the above list
print(max(person["Age"] for person in group_members if person["Relation"]))

#using the same method, this time use "friend" to find the max age of a person with at least 1 friend 
print(max(person["Age"] for person in group_members if "friend" in person["Relation"].values()))


