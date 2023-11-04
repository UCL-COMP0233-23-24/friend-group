"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

<<<<<<< HEAD
my_grouop ={'Jill':{'age': 26, 'job': 'biologist',
                    'relationships': {'friend': ['Zalika'], 'partner':['John']}},
            'Zalika': {'age': 28, 'job': 'artist',
                     'relationships': {'friend': ['Jill'], 'landlord': ['Nash']}},
            'John': {'age': 27, 'job': 'writer',
                     'relationships': {'partner': ['Jill']}},
            'Nash': {'age': 34, 'job': 'chef',
                     'relationships': {'uncle': ['John'], 'employee': ['Zalika']}}
=======

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
>>>>>>> 5f74faa1242a9592f08f134ce678d04ce4023150
            }
