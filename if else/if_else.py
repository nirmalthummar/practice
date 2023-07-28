"""
You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:

"""

a = 330
b = 330

print("A") if a != b else print("=") if a < b else print("B")

# OUTPUT IS B

"""
And
The and keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, AND if c is greater than a:
"""

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OUTPUT IS Both conditions are True
"""Or
The or keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, OR if a is greater than c:"""

a= 500
b = 200
c =600

if a>b or a>c:
  print("one condition is true")


# is and is not keyword Use in if condition
a = 200
b = 200
if a is b:
  print("a is NOT greater than b")

a = 100
b = 150
if a is not b:
  print("Value of a AND b are not same ")


# NESTED IF
x = 22  #int(input("enter a number: "))

if x > 10:
  print(f"{x} is greater than 10")
  if x > 20:
    print(f"{x} is also greater than 20")
  else:
    print(f"but {x} is not greater than 20")

i = 1
while i<6:
  print(i)
  i += 1


# DIVISION Program

# num = int(input("Enter a number :"))

# if num == 0:
#   print(" 0 is not divisible")
# else:
#   for a in range(0,101):
#     if num % a == 0:
#       print(f"{num} is divisible by {a}")

# number = int(input("Enter a number: "))

# if number == 0:
#     print("Cannot divide by 0.")
# else:
#     divisor = 1
#     while divisor <= 100:
#         if number % divisor == 0:
#             print(f"{number} is divisible by {divisor}.")
#         divisor += 1

# a = 0
# if 0 <= a < 20:
#   print("hello")







