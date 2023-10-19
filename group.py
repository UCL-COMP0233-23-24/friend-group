from numpy import mean

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

def find_max_age(people):
    """Return maximum age of people in the group"""
    people=[person for person in people if "age" in group[person].keys()] #to verify that "age" is given, otherwise would get error
    ages=[group[person]["age"] for person in people]
    return max(ages)

print("Maximum age is", find_max_age(["Jill", "Zalika", "John", "Nash"]))

def average_number_relations(people):
    """Return mean number of relations among members of the group"""
    people=[person for person in people if "relations" in group[person].keys()] #to verify that "relations" is given, otherwise would get error
    num_relations=[len(group[person]["relations"]) for person in people]
    return mean(num_relations)

print("Mean number of relations is", (average_number_relations(["Jill", "Zalika", "John", "Nash"])))

def max_age_with_relations(people):
    """Returns maximum age of people in the group with at least one relation"""
    people_with_relation=[person for person in people if "relations" in group[person].keys()] #to verify that "relations" is given, otherwise would get error
    return find_max_age(people_with_relation)

print("Maximum age of people with at least one relation is", max_age_with_relations(["Jill", "Zalika", "John", "Nash"]))

def max_age_with_friends(people):
    """Returns maximum age of people in group with at least one friend"""
    people=[person for person in people if "relations" in group[person].keys()] #to verify that "relations" is given, otherwise would get error
    people_with_friends=[person for person in people if "friend" in group[person].get("relations",{}).values()]
    return find_max_age(people_with_friends)

print("Maximum age of people with at least one friend is", max_age_with_friends(["Jill", "Zalika", "John", "Nash"]))