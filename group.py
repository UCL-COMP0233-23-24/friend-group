"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


class person:
    def __init__(self,name,age,job="",relationship={}):
        self.name=name
        self.age=age
        self.job=job
        self.relationship=relationship
    
    def create_relationship(self,b,relation):
        b.relationship[self.name]=relation
        self.relationship[b.name]=relation
        

    def showall(self):
        print(self.name,self.age,self.job,self.relationship)


Jill = person("Jill",26, "biologist")
Zalika = person("Zalika",28,"artist")
Zalika.showall()
Jill.showall()
Jill.create_relationship(Zalika,"friend")

Zalika.showall()
Jill.showall()

#my_group =
