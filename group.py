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
            self.job = self.name+" is jobless"
        elif isinstance(job,str):
            self.job=job
        else:
            raise TypeError("Error: Invalid job")
        connections={"Friends": [], "Partner": [], "Cousins": [], "Landlord": []}
        self.connections = connections

    #def __repr__(self):
    #    return "Person()"
    

    def conn(self,do_print=1):
        if do_print==1:
            #print(self.name)
            for conn_type in self.connections:
                String=conn_type+": "
                for i in self.connections[conn_type]: String=String+i.name+", "
                #print(String)
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
                return self.connections[conn_type]
            else:     
                raise ValueError("No connection is present between these two people")
        

class Group:
    def __init__(self,members):
        self.members = members

    #def __repr__(self):
    #    return "Group()"

    def add_person(self,person):
        self.members.append(person)
        return self.members

    def forget_person(self,A=Person, B=Person):
        nameslist = []
        for member in self.members: 
            nameslist.append(member.name)
        if ((A.name in nameslist) and (B.name in nameslist)):
            A.forget(B)
            return self.members
        else:
            raise ValueError("Person not in group")
                
    def avg_age(self):
        age_list=[]
        for member in self.members:
            age_list.append(member.age)
        return sum(age_list)/len(age_list)
        
    def max_age(self):
        age_list=[]
        for member in self.members:
            age_list.append(member.age)
        return max(age_list)

    def avg_conn(self):
        connect_len = []
        for people in self.members: 
            part_connect_len = (sum(len(v) for v in people.connections.values()))
            connect_len.append(part_connect_len)
        return sum(connect_len)/len(self.members)
        
    def max_age_over_one_rel(self):
        connect_len = []
        for people in self.members: 
            part_connect_len = (sum(len(v) for v in people.connections.values()))
        filtered = [people for people in self.members if (sum(len(v) for v in people.connections.values()) >0)]
        age_vector = []
        for people in filtered: age_vector.append(people.age)
        return max(age_vector)
                

    def max_age_over_one_friend(self):
        connect_len = []
        for people in self.members: 
            print(people)
        part_connect_len = (sum(len(v) for v in people.connections.values()))
        filtered = [people for people in self.members if (len(people.connections["Friends"]) >0)]
        age_vector = []
        for people in filtered: age_vector.append(people.age)
        print(max(age_vector))
        return max(age_vector)


        
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

#print(Nash)


group1= Group([Jill, John])
print(group1.avg_age())
for members in group1.members: print ("group1  " + members.name)

updated_group1 = group1.add_person(Zalika)

updatedGroup1 = Group(updated_group1)
for member in updatedGroup1.members: print(member.name)


updated_group2 = updatedGroup1.forget_person(Jill,Zalika)
print(updated_group2)
for member in updated_group2: print(member.name + str(member.connections))
updatedGroup2 = Group(updated_group2)


print(updatedGroup2.avg_age())
print(updatedGroup2.max_age())
print(group1.max_age_over_one_rel())
print(updatedGroup1.avg_conn())
print(updatedGroup2.avg_conn())

