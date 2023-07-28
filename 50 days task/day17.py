#############Task 1 User Name Generator

import random
def user_name():
    name=input("Enter your name")[::-1]
    rndm=random.randint(0,9)
    username=name+str(rndm)
    return username

print(user_name())

######Task 2

def sort_length(strings):
    a=sorted(strings,key=len)
    return list(a)
    
    #####second way

    n = len(strings)
    for i in range(1, n):
        key = strings[i]
        j = i - 1
        while j >= 0 and len(strings[j]) > len(key):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
    return strings

    ### Third way

    n = len(strings)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings

l=["Peter","Jon","Andrew"]
print(sort_length(l))




