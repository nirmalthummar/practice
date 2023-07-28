## # FIND MISSING NUMBER FROM LIST ####



def find_missing(lst):
    l1=[]
    for i in range(11):
        if i not in lst:
            l1.append(i)
    return f"This number not in given list:{l1}"


l=[1,2,4,5,7,9,10,8]
print(find_missing(l))