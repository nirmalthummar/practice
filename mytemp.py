# print("hello")
# print("hello")
# print("hello")

# abc = int(input("Enter your age"" "))
# print(type(abc))

# print("good\nmorning ")

# fruits = ["apple","banana","cherry"]
# x,y,z = fruits
# print(x)
# print(y)
# print(z)


# def f():
#     print(s)

# s= "MS Dhoni"
# a = f()
# f = 5
# g=6
# h=7

# print('g',g,'f')

# print('python',end='.')
# print("Django")
# print(z)

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(name)
        
#     def greet(self):
#         print("Hello, my name is " + self.name)
# person1 = Person("Alice")
# person1.greet()   # Output: "Hello, my name is Alice"


# string = "welcome to goa singham"
# print("output is:","-".join(string.split()))

# string = "welcome to india"
# print(string.split(" "))
# print(string)
# a=10
# print(type(a),a+10)

# def calculate_average(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     if count == 0:
#         return 0
#     else:
#         a=total/count
#         return a 
# b = calculate_average([10,20,30])
# print(b)

# string = "abracadabra"
# l = list(string)
# l[4] ="k"
# string = "".join(l)
# print(string)
# print(type(string))

# a =(1,2,3,4)
# print(type(a))
# string1 = "".join(a)
# print(string1)
# print(type(string1))

# print("""
# Capitalize
# """)
# string = "welcome to india"
# print("output is",string.capitalize())


# print("""
# casefold
# """)

# string = "WELCOME TO INDIa"
# print("output is",string.casefold())

# print("""
# ****** center()******
# """)

# string ="INDIA"
# a = print("output is",string.center(10))
# print(len(string))

# print("""
# count()
# """)

# string = "apple mobile made by apple company"
# print("output is",string.count("a"))

# my_string = "hello, how are you?"
# count1 = my_string.count('o')
# count2 = my_string.count('o', 5)
# count3 = my_string.count('o', 5, 10)
# print(count1)  # Output: 4
# print(count2)  # Output: 3
# print(count3)  # Output: 1


# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     return ''.join(l)

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)




# print("""
# ******* endwith()
# """)
# string = "my name is nirmal"
# print("output is",string.endswith("rmal"))
# string = "hello\tworld"# a = string.expandtabs(2)# print(f"lenthofstringis :{len(a)}  *****and string is: {a}")a = 10





# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count



# string = input().strip()
# sub_string = input().strip()

# count = count_substring(string, sub_string)
# print(count)






# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         sub_dtr_length = len(sub_string)
#         sub_dtr_length = sub_dtr_length + 1
#         if string[i:sub_dtr_length] == sub_string:
#             count += 1
#     return count

# Test with a dummy string
# string = "abcdcdcdc"
# sub_string = "cdc"
# count = count_substring(string, sub_string)
# print(count)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "mango"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["mango", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:] = ["Gwawa", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,"watermelon")
# print(thislist)


# my_list = [1, 2, 3, 4, 5]
# my_list.insert(1, my_list.pop(3))
# print(my_list)

# my_list = [3, 4, 2, 15]
# sorted_list = []
# for num in my_list:
#     index = 0
#     while index < len(sorted_list):
#         index += 1
#     sorted_list.insert(index, num)
# print(sorted_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# a= 5
# b=0
# while a>b :
#    b += 1
#    print(b)

# l1 = [2,3,4,5,6,7]
# l1.insert(2,[5,5,5])
# print(l1)

# l2 = [1,3,2,5,7]
# l2.append(9)
# print(l2)

# l1 = ["apple","banana"]
# l2 = ["mango",2,False]
# l1.extend(l2)
# print(l1)

# l3 = ["banana""mango"]
# print("\n", len(l3))

# l1 = ["banana","mango","apple"]
# l1.remove("banana")
# print(l1)

# l1[1] = "kiwi"
# print(l1)

# l1.append("banana")
# print(l1)

# l1.pop(0)
# print(l1)

# l1.pop()
# print(l1)

# del l1[0]
# print(l1)

# l1 = ["apple","banana","mango",]
# del l1

# l1 = ["mango","banana"]
# l1.clear()
# print(l1)

# l1 = ["mango","banana"]
# for x in l1:
#     print(x)

# l1.append("kiwi")
# l1.append("Gwawa")

# for i in range(len(l1)):
#     print(l1[i])

# "Looping using LIst Comprehension"

# l1.append("Watermalon")

# [print(x) for x in l1] 
# """
# ******************************

# LIST COMPREHENSION

# ******************************

# """
# fruits = ["apple","mango","kiwi","Cherry","banana"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# fruits = ["apple","banana","orange","mango","apple"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# x_list = []
# for x in fruits:
#     if x != "banana":
#         x_list.append(x)
#     else:
#         x_list.append("orange")

# print("my list...", x_list)
        

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)


# newlist.sort()
# print(newlist)

# newlist = [100,50,65,82,23]
# newlist.sort()
# print(newlist)
# newlist.sort(reverse=True)
# print(newlist)
# newlist.insert(3,"hello")
# print(newlist)

# l = "hello"
# print(list(l))

" Unpack a Collection"

# fruits = ["apple","banana","mango"]
# x,y,z = fruits
# print(x)
# print(y)

# txt = "hello world"
# txt = txt.replace("h","OOK")
# print(txt)

# l = ["hello world"]

# print(l[0][0:5][::-1])

# a = "Hello, World!"
# b = a.split(",")
# print(b)
# a = "hello"
# b = "world"
# print(a + b)


# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# import time

# progress = 0
# if True:
#     progress = 20

# while progress <= 100:
#     print(f"Progress: {progress}%")
#     progress += 10
#     time.sleep(1)
    

# a = 0
# while 5>=a:
#     print(f"value of a:{a}")
#     a+= 1
#     time.sleep(1)

# txt = "h\tw"

# print(f"txt is :{txt} and Length is : {len(txt)}")

# txt = "Hello\tWorld!"
# print(txt) 

# txt = "hello  \bworld"
# print(txt)

# s1 = "my name is NIRmal"
# x = s1.capitalize()
# print(x)

# txt = "36 is my age."

# x = txt.capitalize()

# print (x)



# s = "my naMe is NIrmal"
# sd = s.casefold()
# print(sd)


# s = "banana"
# x = s.center(10,"+")
# print(x)
# print(len(x))

# s = "I love apples, apple are my favorite fruit"
# print(s.count("apple"))
# print(s.count("a",0,15))

# txt = "My name is Ståle"

# x = txt.encode()

# print(x)

# print(txt.endswith("My",0,2))


# t = "h\te\tl\tl\to"
# x = t.expandtabs(2)
# print(t.expandtabs(8))
# print(t)


# t = "surat city on the banks of river tapi"
# x = t.find("t",6)
# print(x)

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price =49))


# s= "12comerce"
# x = s.isalnum()
# print(x)

# x = s.isalpha()
# print(x)

# x = s.isascii()
# print(x)

# x = s.isdecimal()
# print(x)

# a = ("hello","RRR")
# b = list(a)
# print(b)


# a = ["apple","mango","banana","rasberry","melon"]

# # a[1:2] = ["jamfal",'mango']

# print(a)




# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x) #removed item

# print(thisset) #the set after removal

# newdict = {
#     "brand": "ford",
#     "model": "Mustang",
#     "year" : 1964,
#     "brand": "Mitubisi"
# }
# print(f"""
# id:{id(newdict)}
# type:{type(newdict)}
# data:{newdict}
# brand:{newdict["brand"]}
# length of dictonary:{len(newdict)}


# """)

# di = dict(name = "nirmal", age = 25, state= "gujarat")
# print(di)
# print(type(di))


# print(di["name"])

# x = di.get("age")
# print(x)

# y = newdict.get("model")
# print(y)

# x = di.keys()
# print(x)

"""
===================================================

use of keys ()
<class = dicy_keys>

===================================================

"""

# di["village"] = "abhrampara"
# print(x)
# print(type(x))   

# x= di.values()
# print(x)
# print(type(x))

# di["age"] = 26
# print(x)


# st = "jaysomnath"

# print(st.casefold())

# t =(1,2,3,4)
# print(t[1:-1])

# print(t)

# s ="hello"
# s[2] = "k"
# print(s)




# a = 1,2,3
# print(type(a))

# a =(1)
# print(type(a))

# tup = 1
# tup = tup + tup
# print(tup)

# l =[1,2,3,4,5]
# l.reverse()
# print(l)


# # # Swap first and last element of list
# num_list = [10,15,18,22,20]

# num_list1 = num_list[0], num_list[-1]
# # Now Unpacking

# num_list[-1], num_list[0] = num_list1

# print(num_list)


# Swap function
# def swapList(a):
     
#     # Storing the first and last element
#     # as a pair in a tuple variable get
#     get = a[-1], a[0]
     
#     # unpacking those elements
#     a[0], a[-1] = get
     
#     return a
     
# # Driver code
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

# l1 = [1,2,3,4,5]
# l2 = l1[:]

# print(f"""
#  {id(l1)}
#  {id(l2)}
# """)


# lst = [
# {"value":1},{"value":3},{"value":0},{"value":4}
# ]

# a = [i.values() for i in lst ]
# print(a)
























    
    















































































































# string1 = "python programming language"
# print(f"{string1[0:3]}")















































































