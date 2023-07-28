### TASK 1

from collections import Counter

def repeated_name(names):
    name_counts = Counter(names)
    most_common_name = name_counts.most_common(1)[0][0]
    return most_common_name

# Test case
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
result = repeated_name(name)
print(result)  # Output: "Peter"


### # SECOND WAY

def repeated_name(names):
    count_dict = {}
    max_count = 0
    most_repeated_name = None

    for name in names:
        if name in count_dict:
            count_dict[name] += 1
        else:
            count_dict[name] = 1

        if count_dict[name] > max_count:
            max_count = count_dict[name]
            most_repeated_name = name

    return most_repeated_name

# Test case
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
result = repeated_name(name)
print(result)  # Output: "Peter"


### # THIrD WAY
from statistics import mode

def repeated_name(names):
    most_repeated_name = mode(names)
    return most_repeated_name

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
result = repeated_name(name)
print(result) 

### FOurth WAY ####

def repeated_name(names):
    unique_names = set(names)
    most_repeated_name = max(unique_names, key=lambda x: names.count(x))
    return most_repeated_name

name = ["John", "Pete", "John", "Pete", "Jones", "Peter"]
result = repeated_name(name)
print(result) 


### FIFTH WAY ######


def repeated_name(names):
    most_repeated_name = max(names, key=lambda x: names.count(x))
    return most_repeated_name

name = ["John", "Pete", "John", "Pete", "Jones", "Peter"]
result = repeated_name(name)
print(result) 

###### SIXTH WAYYYY #####

def repeated_name(names):
    count_dict = {}
    for name in names:
        count_dict[name] = count_dict.get(name, 0) + 1
    most_repeated_name = max(count_dict, key=count_dict.get)
    return most_repeated_name

name = ["John", "Pete", "John", "Pete", "Jones", "Peter"]
result = repeated_name(name)
print(result) 