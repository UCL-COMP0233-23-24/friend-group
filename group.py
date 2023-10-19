"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...



my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connects": {
            "Zalika": "friend",
            "John": "partner",
            },
        },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connects": {
            "Jill": "friend",
            },
        },   
    "John": {
        "age": 27,
        "job": "writer",
        "connects": {
            "Jill": "partner",
            },
        },    
    "Nash": {
        "age": 34,
        "job": "chef",
        "connects": {
            "Zalika": "landlord",
            "John": "cousin"
            },
        },
    "Ester": {
        "age": 23,
        "job": "",
        "connects": {
            "Zalika": "landlord",
            "John": "cousin"
            },
        },
    }

for name, content in my_group.items():
    print (name)