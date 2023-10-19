"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {

        "Jill" : 
            {"connection" :{
                "friend" : "Zalika", 
                "partner" : "John"
            },
            "age" : 26,
            "job" : "biologist"},

            
        "Zalika" : 
            {"connection" :{
                "friend" : "Jill"
            },
            "age" : 28,
            "job" : "artist"},


       "John" : 
            {"connection" :{ 
                "partner" : "Jill"
            },
            "age" : 27,
            "job" : "writer"},


        "Nash" : 
            {"connection" :{
                "cousin" : "John", 
                "landlord" : "Zalika"
            },
            "age" : 34,
            "job" : "chef"}    

    }



a = {name: info['age'] for name, info in my_group.items()}

print(a)