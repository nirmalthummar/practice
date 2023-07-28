# def calculator():
#     num1 = None
#     operator = None
#     num2 = None
#     result = None

#     while True:
#         try:
#             if num1 is None:
#                 num1 = float(input("Enter the first number: "))

#             if operator is None:
#                 operator = input("Enter the operator (+, -, *, /): ")

#             if num2 is None:
#                 num2 = float(input("Enter the second number: "))

#             if operator == "+":
#                 result = num1 + num2
#             elif operator == "-":
#                 result = num1 - num2
#             elif operator == "*":
#                 result = num1 * num2
#             elif operator == "/":
#                 if num2 == 0:
#                     raise ZeroDivisionError("Division by zero is not allowed.")
#                 result = num1 / num2
#             else:
#                 raise ValueError("Invalid operator.")

#             break  # Break out of the loop if no exceptions occur

#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             num1 = None
#             operator = None
#             num2 = None
#         except ZeroDivisionError as e:
#             print("Error:", str(e))
#             num1 = None
#             operator = None
#             num2 = None

#     print("Result:", result)


# calculator()

# Method Two

# def calculator():
#     try:
#         num1 = float(input("Enter the first number: "))
#         operator = input("Enter the operator (+, -, *, /): ")
#         num2 = float(input("Enter the second number: "))

#         if operator == "+":
#             result = num1 + num2
#         elif operator == "-":
#             result = num1 - num2
#         elif operator == "*":
#             result = num1 * num2
#         elif operator == "/":
#             if num2 == 0:
#                 raise ZeroDivisionError("Division by zero is not allowed.")
#             result = num1 / num2
#         else:
#             raise ValueError("Invalid operator.")

#         print("Result:", result)

#     except ZeroDivisionError as e:
#         print("Error:", str(e))
#     except (ValueError, NameError) as e:
#         print("Error:", str(e))


# calculator()


# practice

# num1=5.0
# num2=4.0
# result=9.0
# if num1.is_integer() and num2.is_integer() and result.is_integer():
#     result = int(result)  # Convert result to integer when both inputs are integers
#     print(result)


# Task 2

# def multiply_words(s):
    # words = s.split()
    # result = 1

    # for word in words:
    #     if word.islower():
    #         result *= len(word)

    # return result
    

# Test cases
# s1 = "love live and laugh"
# print(multiply_words(s1))  # Output: 240

# s2 = "Hate war love Peace"
# print(multiply_words(s2))  # Output: 12


