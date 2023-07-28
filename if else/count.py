def register_check(student):
    # count = 0
    # for i in student.values():
    #     if i == "yes":
    #         count += 1
    # return count

    # count = student.values().count("yes")
    # return count
    count = sum(1 for tiem in student.values() if tiem == "yes")
    return count

register = {
    "micle": "yes",
    "james": "yes",
    "root": "no",
    "cook": "yes"
}

result = register_check(register)
print(result)

def lowercase_name(name):

    pass


print(lowercase_name(["kerry", "direl", "Marry", "ronny", "Tommy", "john", "wick", "adam"]))
