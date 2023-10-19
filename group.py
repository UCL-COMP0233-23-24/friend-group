"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
my_group = [

    {
        "name": "Jill",
        "age": "26",
        "job": "biologist",
        "relationship": {"partner": ["John"],"friend": ["Zalika"]},
    },
    {
        "name": "Zalika",
        "age": "28",
        "job": "cleaner",
        "relationship": {"friend": ["Jill"],"landlord": ["Nash"]},
    },
    {
        "name": "John",
        "age": "27",
        "job": "cleaner",
        "relationship": {"partner": ["Jill"],"cousin":["Nash"]},
    },
    {
        "name": "Nash",
        "age": "34",
        "job": "cleaner",
        "relationship": {"friend": ["Zalika"],"cousin":["John"]},
    },
]

