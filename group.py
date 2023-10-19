
## -- STYLEGUIDE -- ##
"""
my_group = {
    <name> : {
        "age" : <age>,
        "job" : <job>,
        "connections" : {
            <name>:[<relation>, <relation>]
        },
    },
}
"""

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'connections': {
            'Zalika': 'friend', 
            'John': 'partner'
        }
    },
    'Zalika': {
        'age': 28,
        'job': 'artist',
        'connections': {
            'Jill': 'friend', 
            'Nash': 'landlord'
        }
    },
    'John': {
        'age': 27,
        'job': 'writer',
        'connections': {
            'Jill': 'partner',
            'Nash': 'cousin'
        }
    },
    'Nash': {
        'age': 27, 
        'job': 'chef', 
        'connections': {}
    }
}