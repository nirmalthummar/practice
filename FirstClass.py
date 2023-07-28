print("""
*********************************************
    Illustrating First Class Functions
*********************************************
""")


def UpperCase(txt):
    return txt.upper()

uc = UpperCase

a = uc("hello World")

# a = UpperCase("hello")

print(a)



print("""
*********************************************
Function can be passed as arguments to other functions
*********************************************
""")

def OddEven(number):
    if number % 2 == 0:
        return f"{number} is even number."
    else:
        return f"{number} is odd number."
    

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
        return f"{num} is prime number"
    else:
        return f"{num} is not prime number"



def CheckNumber(number, checkMethod=PrimeNumber):
    return checkMethod(number)


a = CheckNumber(10)
print(a)


