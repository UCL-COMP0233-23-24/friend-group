"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill' : {
        'age' : 26,
        'job' : 'biologist',
        'relationships' : {
            'friend' : 'Zalika',
            'partner' : 'John',
            'cousin' : '',
            'landlord' : ''
        }
    },
    'Zalika' : {
        'age' : 28,
        'job' : 'artist',
        'relationships' : {
            'friend' : 'Jill',
            'partner' : '',
            'cousin' : '',
            'landlord' : 'Nash'   
        }
    },
    'John' : {
        'age' : 27,
        'job' : 'writer',
        'relationships' : {
            'friend' : '',
            'partner' : 'Jill',
            'cousin' : 'Nash',
            'landlord' : ''   
        }
    },
    'Nash' : {
        'age' : 34,
        'job' : 'chef',
        'relationships' : {
            'friend' : '',
            'partner' : '',
            'cousin' : 'John',
            'landlord' : ''   
        }
    }
}

{name: person['relationships'] for name, person in my_group.items()}
print(my_group)
