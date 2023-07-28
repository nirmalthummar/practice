print("""
*********************************************
            Map()
*********************************************
""")



def square(num):
    return num * num


numList = [1,2,3,4,5,6,7,8,9]

result = map(square,numList)

print(tuple(result))




def squareDSA(*num):
    list1 = []
    for i in num:
        a = i * i
        list1.append(a)

    return list1



def squareDSACompr(*num):
    # list1 = [i * i for i in num]
    return [i * i for i in num]