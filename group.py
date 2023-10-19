"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {

    'Jill' : {
        'age': '26',
        'job': 'biologist',
        'connections' : {
            'friends' : 'Zalika',
            'partner' : 'John',
            'landlord' : '',

        }
         
    },

    'Zalika' : {
        'age': '28',
        'job': 'artist',
        'connections' : {
            'friends' : 'Jill',
            'partner' : '',
            'landlord' : 'Landlord',

        }
         
    },

    'John' : {
        'age': '27',
        'job': 'writer',
        'connections' : {
            'friends' : '',
            'partner' : 'Jill',
            'landlord' : '',

        }
         
    },

    'Nash' : {
        'age': '34',
        'job': 'chef',
        'connections' : {
            'relationship' : {
                'cousin' : 'John'
            },
            'friends' : '',
            'partner' : '',
            'landlord' : ''

        }
         
    }
}
