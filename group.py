"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill={"name":"Jill","age":26,"Job":"Biologist","Relation":{"Zalika":"friend","John":"partner"}}
Zalika={"name":"Zalika","age":28,"Job":"artist","Relation":{"Jill":"friend","Nash":"renter"}}
John={"name":"John","age":27,"Job":"writer","Relation":{"Jill":"partner","Nash":"uncle"}}
Nash={"name":"Nash","age":34,"Job":"chef","Relation":{"John":"cousin","Zalika":"landlord"}}


def forget(person1,person2):
    del person1['Relation'][person2['name']]
    del person2['Relation'][person1['name']]


def add_person(name,age,job,relations):
    person = {"name":name, "age":age, "Job":job,"Relation":relations}
    return person


def average_age(group):
    total_age=0
    total_person=0
    for i in group:
        total_age += i['age']
        total_person +=1
    
    return total_age / total_person



my_group =[]
my_group.append(Jill)
my_group.append(Zalika)
my_group.append(John)
my_group.append(Nash)
print(my_group)

forget(Jill,Zalika)
print(Jill)
print(Zalika)

Dick = add_person("Dick", 26, "writer", {})
my_group.append(Dick)
print(Dick)

print(average_age(my_group))



