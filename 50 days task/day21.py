########Task 1

def make_tuple(a,b):
    # a=[(i,j) for i,j in zip(a,b)]
    # return a
    n=[]
    for i in range(len(a)):
        n.append((a[i],b[i]))
    print(n)



a=[1,2,3,4]
b=[5,6,7,8]

print(make_tuple(a,b))

############ task 2

def even_or_average():
    l=[]
    while True:
        
        l.append(int(input("Enter a number")))
        if len(l)==5:
            break
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i)
    if len(l1)==0:
        return sum(l)/len(l)
    else:
        return max(l1)

    #################Second method

    numbers = [int(input("Enter a number: ")) for _ in range(5)]
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return sum(numbers) / len(numbers)

    ##########Third Method

    numbers = []
    for _ in range(5):
        numbers.append(int(input("Enter a number: ")))
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return sum(numbers) / len(numbers)

    ############## Fourth Method 

    numbers = []
    count = 0
    while count < 5:
        numbers.append(int(input("Enter a number: ")))
        count += 1
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return sum(numbers) / len(numbers)

    
print(even_or_average())