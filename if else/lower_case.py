# def lowercase_name(name):
#     emp_list = [l for l in name if l.islower()]
#     emp_list.sort(reverse=True)
#     return emp_list

# print(lowercase_name(["kerry", "direl", "Marry", "ronny", "Tommy", "john", "wick", "adam"]))

# lst = [
# {"value":1},{"value":3},{"value":0},{"value":4}
# ]

# a = [lst[0].values(),lst[1].values(),lst[2].values(),lst[3].values()]
# b = list(a)
# c=[]
# for i in b:
#    print( i.values())

# print(c)

# fruits = ["accc","jkdjkjd","hjh"]
# a,b,c = fruits
# print(a,b,c)
# print("hello ram",sep=" ")
# print("world")

# print('*', "abcde".center(8), '*')

# list1 = [1, 3]
# list2 = list1[:]
# list1[0] = 4
# print(list2)

# i = 0
# while i < 5:
#     print(i,end="=")
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)



# my_list = "hello world"
# print(dir(my_list))  # displays attributes and methods of the list object

# print("Hello {0[0]} and {0[1]}".format(('foo', 'bin')))

# t =(1,2,3,4)

# print(t[0])
# help(id)
a = """my
       name is
       nirmal
"""
# file_path = r'C:\Users\SimplifyVMS\Desktop\Nirmal\practice\if else\lower_case.py'

# with open(file_path, 'r') as file:
#     lines = file.readlines()

# vertical_length = len(lines)
# print(vertical_length)

# s =set("hello")
# b=s.copy()
# print(s)
# print(b)

# s='The {} side {1} {2}'.format('bright', 'of', 'life')
# print(s)


# Python program to illustrate functions
# can be treated as objects
# def shout(text="hello"):
#     return text.upper()
 
# # print(shout('Hello'))
 
# yell = shout
 
# print(yell())



# def mk(x):
#     def mk1():
#         print("Decorated")
#         x()
#     return mk1

# @mk
# def mk2():
#     print("Ordinary")
# mk2()
# p = mk(mk2)
# p()


# def ordi():
# 	print ("Ordinary")

# print(ordi())

# a = 0%2
# print(a)  #0
# b=2%0
# print(b) # ZeroDivisionError: integer division or modulo by zero



# def decf(x):
#     print("x...", x)
#     def f1(a, b):
#         print("hello")
#         if b==0:
#             print("NO")
#             return
#         mainf(a, b)
#     return f1

# @decf
# def mainf(a, b):
#     print("1")
#     return a%b
# mainf(4,1)

x = "abcdef"
# i = "a"
# while i in x:
#     x = x[:-1]
#     print(i, end = " ")
# y = x[5:-1]
# print(y)
# my_list = [1, 2, 3, 4, 5]
# result = ', '.join(str(x) for x in my_list)
# print(result)  # Output: 1, 2, 3, 4, 5
# l = list("hello")
# k=''.join(i.upper() for i in l)
# print(k)

# print('new''line')
# print(0xA + 0xB + 0xC)
s = "HEllO"
sd = "nirmal"
# y=s.partition("k")
# print(y)
# a=s.__add__(sd)
# print(a)

# print("%s*%s" %(s,sd))
# print(s.casefold())
# t= (1)
# print(type(t))
# l = ["amita","Amit",123]
# print(max(l))

# z =0
# y=10
# x=y<z and z>y or y>z and z<y
# print(x)
# # y= True
# print(True)


# x =2.0
# y=4.0
# print(y**0.5)

# for i in range(-1,-2):
#     print(i)

# tup = (1,2,4,8)
# tup = tup[-2:-1]
# print(tup)
# tup = tup[-1]
# print(tup)

# def f(x):
#     if x ==0:
#         return 0
#     return x + f(x-1)

# print(f(3))


# dictionary = {}
# my_list = ["a","b","R","d"]

# for i in range(len(my_list)-1):
#     dictionary[my_list[i]] = (my_list[i],)

# print(dictionary)
# # for i in sorted(dictionary.keys()):
# #     k = dictionary[i]
# #     print(k[0])

# y = 2+3*5.
# print(y)

# l=[0,1,2,3]
# l.insert(-1,l[0])
# print(l)


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

# def my_discount():
#     price = int(input("enter a price"))
#     discount = int(input("enter a discount:"))



        
    
        








