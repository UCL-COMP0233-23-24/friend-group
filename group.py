"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
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

# 1. the maximum age of people in the group
def max_age(group):
    max_age = 0
    for person in group:
        max_age = max_age if max_age > group[person]['age'] else group[person]['age']
    return max_age

print(max_age(group))

# 2. the average (mean) number of relations among members of the group
def average_rel(group):
    avg = 0
    for person in group:
        avg += len(group[person]['relations'])
    return avg/len(group)

print(average_rel(group))


# 3. the maximum age of people in the group that have at least one relation
def max_age_rel(group):
    max_age = 0
    for person in group:
        if len(group[person]['relations']) >= 1:
            max_age = max_age if max_age > group[person]['age'] else group[person]['age']
    return max_age

print(max_age_rel(group))

# 4. [more advanced] the maximum age of people in the group that have at least one friend
def max_age_friend(group):
    max_age = 0
    for person in group:
        if 'friend' in group[person]['relations'].values():
            max_age = max_age if max_age > group[person]['age'] else group[person]['age']
    return max_age

print(max_age_friend(group))