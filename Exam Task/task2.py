## # SECOND RUNNER UP NUMBER ## #

def find_second_runner(dictonary):
    l=[]
    for i in dictonary.values():
        l.append(i)
    a=sorted(l)[-2]
    return f"second runnner up number is {a}"


dict1={"nirmal":100,"john":90,"wick":80,"Thor":70}
print(find_second_runner(dict1))