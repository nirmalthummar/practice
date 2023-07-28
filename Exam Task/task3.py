def sequence(string):
    a=string.replace(",","")
    #b=",".join(a)
    print(list(a))
    print(tuple(a))
    


number= "1,2,3,4"
print(sequence(number))

