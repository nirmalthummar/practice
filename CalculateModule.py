abc = "Hello"


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
    
class Calculate:

    divied_number = 10

    def __init__(self, num):
        """
        Remove duplicate value using for loop
        """
        self.list1 = []
        for i in num:
            if i not in self.list1:
                self.list1.append(i)

    def addition(self):
        count  = 0

        for i in self.list1:
            count += i

        return count