print("""
**************************************
    Error & Exception	Handling
**************************************
""")

try:

    # num1 = int(input("Enter the number 1 : "))
    # num2 = int(input("Enter the number 2 : "))

    num1 = 0
    num2 = 2

    result = num1 / num2
    print(f"\nResult : {result}")

# except Exception as e:
#     print(e)


except ZeroDivisionError as Z:
    print("Hello",Z)

except TypeError as t:
    print("Error",t)

except:
    print("Please find the error")

print("""
**************************************
            Example - 2 
**************************************
""")

def OddEven(num1):

    try:
        if num1 % 2 == 0:
            return f"{num1} is Even Number."
        else:
            return f"{num1} is odd Number."
    # except TypeError:
    #     return f"Please find the error"
    except Exception as e:
        try:
            if int(num1) % 2 == 0:
                return f"{num1} is Even Number>>>>>>>>>>>>>>>."
            else:
                return f"{num1} is odd Number>>>>>>>>>>>>>>>.."
        except TypeError as te:
            return f"{te}>>>>>>>>>>>>>>"
        except ValueError as ve:
            return f"ValueError :>>>>>>>>>>>>>> {ve}"
        # return f"Error : {e}"
    

a = OddEven(2)
print(a)





print("""
**************************************
            Example - 3 - Finally  
**************************************
""")



try:

    # num1 = int(input("Enter the number 1 : "))
    # num2 = int(input("Enter the number 2 : "))

    num1 = 10
    num2 = "2"

    result = num1 / num2
    print(f"\nResult : {result}")


except Exception as e:
    print(e)
finally:
    print("this is a finally Block.")
    a = OddEven(10)
    print("Call oddven block in finally block >> ",a)
    try:
        num1/num2
    except:
         print("Except Block Hello")





print(f"\n\n\n******************* End **********************")