print("""
*********************************************
            filter()
*********************************************
""")

def OddEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def PrimeNumber(num):
    prime = True
    if num == 1:
        return f"{num} is Prime Number."
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    if prime:
        return True
    else:
        return False


a = filter(OddEven, [1,2,3,4,5,6])


print(list(a))
# print(a)