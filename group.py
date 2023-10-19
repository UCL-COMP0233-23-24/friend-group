"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill={"name":"Jill","age":26,"Job":"Biologist","Relation":[{"Zalika":"friend"},{"John":"partner"}]}
Zalika={"name":"Zalika","age":28,"Job":"artist","Relation":[{"Jill":"friend"},{"Nash":"renter"}]}
John={"name":"John","age":27,"Job":"writer","Relation":[{"Jill":"partner"},{"Nash":"uncle"}]}
Nash={"name":"Nash","age":34,"Job":"chef","Relation":[{"John":"cousin"},{"Zalika":"landlord"}]}


my_group =[]
my_group.append([Jill,Zalika,John,Nash])
print(my_group)