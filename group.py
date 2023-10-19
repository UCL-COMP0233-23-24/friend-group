"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill = {"Name": "Jill",
        "Age": 26, 
        "Jobs": "Biologist",
        "Friend": "Zalika",
        "Partner": "John",
        "Cousin": "",
        "Landlord": ""}

Zalika = {"Name": "Zalika",
        "Age": 28,  
        "Jobs": "Artist",
        "Friend": "Jill",
        "Partner": "",
        "Cousin": "",
        "Landlord": "Nash"}

John = {"Name": "John",
        "Age": 27,  
        "Jobs": "Writer",
        "Friend": "",
        "Partner": "Jill",
        "Cousin": "Nash",
        "Landlord": ""}

Nash = {"Name": "Nash",
        "Age": 34,  
        "Jobs": "Chef",
        "Friend": "",
        "Partner": "",
        "Cousin": "John",
        "Landlord": ""}

my_group = [Jill, Zalika, John, Nash]
print(my_group)
