"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}




my_group0 = [{'name': 'Jill', 'age': 8, 'job': 'biologist',
             'relationship': {'partner':['John']}},
            {'name': 'Zalika', 'age':28, 'job': 'artist',
             'relationship': {'friends':['Jill']}},
            {'name': 'John', 'age': 27, 'job': 'writer',
             'relationship': {'partner': ['Jill']}},
            {'name': 'Nash', 'age': 34, 'job': 'chef',
             'relationship': {'cousin':['John'], 'landlord':['Zalika']}}
            ]




my_grouop1 ={'Jill':{'age': 8, 'job': 'biologist',
                    'relationships': {'partner': ['John']}},
            'Zalika': {'age': 28, 'job': 'artist',
                     'relationships': {'friends': ['Jill']}},
            'John': {'age': 27, 'job': 'writer',
                    'relationships': {'partner': ['Jill']}},
            'Nash': {'age': 34, 'job': 'chef',
                    'relationships': {'cousin':['John'], 'landlord':['Zalika']}}
            }