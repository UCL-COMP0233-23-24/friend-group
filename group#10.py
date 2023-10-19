my_group = {'Jill':{'age':'26','job': 'biologist','friend':'Zalika','partner':'John'},
    'Zalika':{'age':'28','job': 'artist','friend':'Jill'},
    'John':{'age':'27','job': 'writer','partner':'Jill'},
    'Nash':{'age':'34','job': 'chef','cousin':'John','Landlord':'Zalika'},
    'Huangmou':{'age':'21'}
}


# forget function has completed
def forget(search_number, search_man):
    for student_id, subjects in my_group[search_man].items():
        if search_number in subjects:
            my_group[search_man].pop(student_id)
            break
    for student_id, subjects in my_group[search_number].items():
        if search_man in subjects:
            my_group[search_number].pop(student_id)
            print(my_group)
            break
forget('Zalika','Jill')


# add_person function has completed
def add_person(name,age,job,relation):
    my_group[name]={'age':age,'job':job,'relation':relation}
    print(my_group)
add_person('fangfang','21','student','huangmou friend')


# averge_age calculate has completed
def averge_age(grouplist):
    studentlist = []
    for student in grouplist:
        studentlist.append(student)
    agelist = []
    for i in range(len(studentlist)):
        agelist.append(grouplist[studentlist[i]]['age'])
    agelist = [int(age) for age in agelist]
    averge_age = sum(agelist)/len(studentlist)
    print(averge_age)

averge_age(my_group)




