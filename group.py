"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={
            "Jill": [26,"biologist",{"friend": "Zalika","partner": "John"}],
            "Zalika": [28, "artist", {"friend": "Jill"} ],
            "John": [27,"writer", {"partner": "Jill", "cousin": "Nash"}],
            "Nash": [34,"chef", {"cousin": "John", "landlord": "Zalika"}]

        }
#print(my_group)
    

class Person:
    def __init__(self,name=str, age=float, job=""):
        self.name = name
        self.age = age
        if not job:
            self.job = self.name+" is homeless :("
        elif isinstance(job,str):
            self.job=job
        else:
            raise TypeError("Error: Invalid job")
        connections={"Friends": [], "Partner": [], "Cousins": [], "Landlord": []}
        self.connections = connections
        
    def conn(self,do_print=1):
        if do_print==1:
            print(self.name)
            for conn_type in self.connections:
                String=conn_type+": "
                for i in self.connections[conn_type]: String=String+i.name+", "
                print(String)
        else: return self.connections
        
        
    def add_connection(self, new_person, conn_type=str):
        if conn_type in self.connections:
            self.connections[conn_type].append(new_person)
            
            if conn_type in ["Friends", "Cousins", "Partner"]:
                new_person.connections[conn_type].append(self)  
        else:
            raise TypeError("Error: Invalid connection type")
            
    def forget(self,person):
        for conn_type in self.connections:
            if person in self.connections[conn_type]:
                self.connections[conn_type].remove(person)
        
        
class Group:
    def __init__(self,members):
        self.members = members
    
    def add_person(self,person):
        self.members.append(person)
        
    def forget_person(self,A=str,B=str):
        for i in self.members:
            if i.name==A:
                i.forget(A)
            else:
                raise ValueError("Person not in group")
                
    def avg_age(self):
        Age=[]
        for i in self.members:
            Age.append(i.age)
        return sum(Age)/len(Age)
        
        
        
Jill=Person("Jill", 26, "biologist")
Zalika=Person("Zalika", 28, "artist")   
John=Person("John", 27,"writer")
John.add_connection(Jill,"Partner")
Nash=Person("Nash", 34, "chef")
John.add_connection(Nash,"Cousins")
Nash.add_connection(Zalika,"Landlord")

Jill.add_connection(Zalika,"Friends")

Jill.conn()
Zalika.conn()
John.conn()
Nash.conn()

    