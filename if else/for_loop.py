# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = 5  # number of rows
# spaces = n - 1

# for i in range(1, n + 1):
#     print(' ' * spaces + '*' * i)
#     spaces -= 1

# l1 = set([7,2,3,5,8,4,7,6,5,4])
# l = list(l1)

# for i in range(l[0],l[-1]):
#     print(i)

# a = l[0]
# print(a)
       



    



# def sqrt(number):
#     if number == 0 or number == 1:
#         return number

#     guess = number / 2  # Initial guess

#     while True:
#         new_guess = (guess + number / guess) / 2
#         if abs(guess - new_guess) < 0.0001:  # Adjust the threshold as needed
#             return new_guess
#         guess = new_guess

# # Example usage
# num = 10
# result = sqrt(num)
# print(f"The square root of {num} is: {result}")




# import math

# def divide_or_square(number):
#     if number%5 ==0:
#         return print(f"sqrt of {number} is :{format(math.sqrt(number),'.2f')}")
#     else:
#         return print(f"remainder of {number} is: {math.remainder(number,5)}")
    

# divide_or_square(int(input("enter a number")))



# def longest_value(dictionary):
#     longest = None
#     longest_length = 0

#     for value in dictionary.values():
#         if len(value) > longest_length:
#             longest = value
#             longest_length = len(value)

#     return longest

# fruits = {"fruit":"apple","color":"greennn","weight":"fivekg"}
# print(longest_value(fruits))

# def longest_value(dictionary):
#     longest = None
#     longest_length = 0

#     for value in dictionary.values():
#         current_length = len(value)  # Calculate the current length
#         if current_length > longest_length:  # Use '>=' instead of '>'
#             longest = value
#             longest_length = current_length
#               # Exit the loop after finding the first longest value

#     return longest



# def longest_value(dictionary):
#     longest = max(dictionary.values(), key=len)
#     return longest



# fruits = {"fruit": "apple", "color": "green", "weight": "lakkjj"}
# result = longest_value(fruits)
# print(result)  


# def register_check(data):

#     count= 0
#     for i in data.values():
#         if i == "yes":
#             count += 1
#     return count


# register = {
#     "micle":"yes",
#     "james":"yes",
#     "root":"no",
#     "cook":"yes"
# }

# result = register_check(register)
# print(result)


# def lowercase_name(name):
#     emp_list = []
#     for i in name:
#         if i == str.lower(i):
#             emp_list.append(i)
    
#     emp_list.sort(reverse=True)
#     return tuple(emp_list)


    
# print(lowercase_name(["kerry","direl","Marry","ronny","Tommy","john","wick","adam"]))

# def check_duplicates(lst):
#     if len(lst) == len(set(lst)):
#         return "No duplicates"
#     else:
#         duplicates = []
#         unique_items = set()
#         for item in lst:
#             if item not in unique_items:
#                 unique_items.add(item)
#             else:
#                 duplicates.append(item)
#         return duplicates

# fruits = ['apple', 'orange', 'banana', 'mango', 'banana', 'apple','kiwi','mango']
# names = ['yamaha', 'hero', 'honda', 'suzuki']

# print(check_duplicates(fruits))
# print(check_duplicates(names))


# import math

# def sqr(x):
#     result= math.sqrt(x) if x%5 == 0 else x%5 
#     return result

# print(sqr(3))

# def register_check(data):
#     count = list(data.values()).count("yes")
#     return count

# register = {
#     "micle": "yes",
#     "james": "yes",
#     "root": "no",
#     "cook": "yes"
# }

# result = register_check(register)
# print(result)

# def find_prime(number):
#     primen = True
#     prime_numbers=[]
#     no_prime_number=[]

#     for num in number:
        
#         if num == 1:
#             no_prime_number.append(num)
#         else:
#             for j in range(2,num):
#                 if num % j ==0:
#                     primen = True
#                     break
#     if primen==True:
#         no_prime_number.append(num)
#     else:
#         prime_numbers.append(num)

def find_prime(numbers):
    prime_numbers = []
    no_prime = []
    
    for num in numbers:
        if num == 1:
            no_prime.append(num)
        elif num == 2:
            no_prime.append(num)
        else:
            prime = True
            for j in range(2,num):
                if num % j == 0:
                    prime = False
                    break
            if prime:
                prime_numbers.append(num)
            else:
                no_prime.append(num)

    return prime_numbers, no_prime

abc = (1,2,3,4,5,6,7,8,9,10,11,12,13,200,181,192)
print(find_prime(abc))


#     return prime_numbers,no_prime_number


# abc = (3,4)

# print(find_prime(abc))



























