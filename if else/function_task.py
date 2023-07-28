# def only_floats(a,b):
#     count=0
#     l =[a,b]
#     for i in l:
        
#        if type(i)== float:
#             count += 1
#     return count
       
#        a = len([i for i in [a,b] if type(i)==float])
#        return a
    
    

# print(only_floats(3.7,2))


# def word_index(lst):
   
#     # a = max(lst,key=len)
#     # return lst.index(a)
# print(word_index(["ab","ab","ab","ad","abc"]))


# def word_index(lst):
#     longest_index = max(range(len(lst)), key=lambda i: len(lst[i]))
#     print(longest_index)

    
#     return longest_index

# print(word_index(["ab", "ab", "abcdefg", "ad", "abcd"]))


# discoun___function

# def my_discount():
#     price = int(input("enter a price"))
#     discount = int(input("enter a discount in(percentage) %:"))/100
#     price_after_discount = price -(price*discount)
#     return price_after_discount

# print(my_discount())

# function______for__________student______zender

# def student_zender(slist):
#     stu = {}
#     lst=[]
#     for i in slist:
        
#         if i.lower() in stu:
#             stu[i.lower()]+=1
#         else:
#             stu[i.lower()]=1
#     for a,v in stu.items():
#         lst.append((a,v))
#     return lst

# student= ["male","male","female","Female","male","female","male","female","male"] 
# print(student_zender(student))

# def student_zender(slist):
#     stu = {i.lower(): slist.count(i) for i in slist}
#     result = [(k.capitalize(), v) for k, v in stu.items()]
#     return result

# student = ["male", "male", "female", "Female", "Male", "female", "male", "female", "male"]
# print(student_zender(student))


# def student_zender(slist):
#     stu = {}
#     for i in slist:
#         if i.lower() in stu:
#             stu[i.lower()] += 1
#         else:
#             stu[i.lower()] = 1
    
#     result = [(k.capitalize(), v) for k, v in stu.items()]
#     return result

# student = ["male", "male", "female", "Female", "Male", "female", "male", "female", "male"]
# print(student_zender(student))

# def user_name(email):
    
#     return f"user name : {email.split('@')[0]}"

# print(user_name(input("Enter your email : ")))

# def zerod_number(lst):
#     lst[0],lst[-1]= 0,0
#     return lst


# l = [8,97,8,5,6]
# print(zerod_number(l))


# def string_range(num):
#     l =[]
#     for i in range(num):
#         l.append(str(i))
#     return ".".join(l)

# print(string_range(int(input("Enter a single number :"))))
# l ="nirmal"
# a = "-".join(l.split('-'))
# print(a)

# def dic_name(lst):
#     num={}
#     for i in lst:
#         if i.startswith("S"):
#             if i in num:
#                 num[i] +=1
#             else:
#                 num[i]=1
            
#     return num


# names = ["nathan","rahul","Sagar","kk","Sanjay","Sagar"]
# print(dic_name(names))

# def dic_name(lst):
#     num = {name: lst.count(name) for name in lst if name.startswith("S")}
#     return num


# names = ["nathan", "rahul", "Sagar", "kk", "Sanjay", "Sagar"]
# print(dic_name(names))

# def hide_password(name):
#     l=[]
#     for i in name:
#         l.append("*")
#     return f"""{''.join(l)} password is {len(name)} character long"""
        

# print(hide_password("nirmal"))


# def convert_number(lst):
#     new_l=[]
#     for i in lst:
#         new_l.append(str(f"{i:,}"))
#     return new_l
     
#     return [str(f"{i:,}") for i in lst]
# l=[156525,2505000,654897789023,456789]
# print(convert_number(l))

# def equal_string(a,b):
#     # a1= sorted(a)
#     # a2=sorted(b)
#     if sorted(a)==sorted(b):
#         return True
#     else:
#         return False

# print(equal_string("nirma","niram"))


# def swape_value(lst):
#     lst[0],lst[-1]=lst[-1],lst[0]
#     return lst

# l=[7,94,5,3,9]
# print(swape_value(l))

# def count_dots(strd):
    # a= strd.count(".")
    # return a
    # count=0
    # for i in strd:
    #     if i== ".":
    #         count +=1
    # return count
#     return len([i for i in strd if i=="."])

# s="n.ir.m..al."
# print(count_dots(s))

# def age_in_minutes():
#     a = input("Enter a your birth year in 4 digit")
#     while len(a)<=3 or len(a)>5:
#         a = input("Enter a your birth year in 4 digit")
#     b= int(a)
#     while b<1900 or b>2023:
#         b= int(input("enter year between 1900 to 2023:"))
#     print(b)

# l=['a','5','c','d']
# l.clear()

# num1 = [0, 1, 2, 3]
# num2= [4, 5,6]
# num1.extend([i for i in range(4,7)])
# print('Numbers:', num1)
# print(num2)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
# import datetime

# def age_in_minutes():
#     while True:
#         year_of_birth = input("Enter your year of birth (4 digits): ")
        
#         if len(year_of_birth) != 4:
#             print("Invalid input. Please enter a four-digit year.")
#         else:
#             try:
#                 year_of_birth = int(year_of_birth)
#                 current_year = datetime.datetime.now().year
                
#                 if year_of_birth < 1900:
#                     print("Invalid input. Please enter a valid year.")
#                 elif year_of_birth > current_year:
#                     print("Invalid input. Please enter a year before the current year.")
#                 else:
#                     age_minutes = (current_year - year_of_birth) * 365 * 24 * 60
#                     print("You are", age_minutes, "minutes old.")
#                     # break
#                     return age_minutes
                    
#             except ValueError:
#                 print("Invalid input. Please enter a valid year.")

# age_in_minutes()


# def your_vat():
#     while True:
#         try:
#             price= float(input("Enter your price:"))
#             vat=float(input("enter a VAT:"))
#             # if type(price) != float:
#             #     print("hello")
#             # elif type(vat) != float and int:
#             #     print("correct")
            
#             # else:
#             mrp= price+price*vat/100
#             return f"Final Price is:{mrp}"

           
            
#         except ValueError:
#             print("Enter valid price or VAT:")

# print(your_vat())

# def flat_list(lst):
#     l=[]
    
#     if len(lst)>1:
#         for j in lst:
#             l.append(j)
#         return l
#     else:
#         return lst[0]
# print(flat_list([[1,2,3,4],[8,9],10]))


# def flat_list(lst):
#     return sum(lst, [])

# print(flat_list([[1,2,3,4]]))

# def monthly_salary():
#     teacher_name = input("Enter Teacher's Name-:")
#     lecture = int(input("Enter a lecture taught by teacher-:"))
#     per_lec_charge=20
#     overtime_charge=25
#     if lecture>100:
#         return f"Techer name:{teacher_name}\nTotal Lecture:{lecture}\nGroos salary:{(lecture-100)*25+100*20}"
#     else:
#         return f"Techer name:{teacher_name}\nTotal Lecture:{lecture}\nGross salary:{lecture*20}/-$"


# print(monthly_salary())

# def same_in_reverse(name):
#     a = list(name)
    
#     list.reverse(a)
#     print(a)
#     if list(name) == a:
#         return True
#     else:
#         return False

# string = input("Enter a string To check reverse:")
# print(same_in_reverse(string))


# *********************** day 15 What is My Age *************************

# def your_age(name_age):
    
#     name = input("Enter Your Name:").lower()
#     if name in name_age:
#         return f"Hy {name} your age is {name_age[name]}"
#     else:
#         add_name= int(input("your Name not in list,Enter your age"))
#         name_age[name]=add_name
        
#         print(f"Hi,{name} your age is {name_age[name]}")
#         return name_age
    

# name_age = {"jane":23,"nirmal":25,"raghav":20,"john":28}
# name_age=your_age(name_age)


"""********************************DAY 16*********************************"""

def sum_list(lst):
    # count=0
    # for num in lst:
    #     for j in num:
    #         count +=j
    # return f"tolal sum of nested list is:{count}"

    """++++++++++++++ Second Way++++++++++++"""
    # a = sum([num for sublist in lst for num in sublist])
    # return a
    if isinstance(lst, list):
        return sum(sum_list(sublist) for sublist in lst)
    else:
        return lst

l=[[2,4,6],[3,4,6],[5,1]]
total=sum_list(l)
print(total)





    















