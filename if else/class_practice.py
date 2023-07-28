from math import sqrt

class dayone:

    def __init__(self):
        print("Day One--Parent")
        self.fname="Parent--RAM"
        print("Parent-Name",self.fname)
        self.number= 10
        self.dictonary= {"fruit":"apple","color":"green"}
        self.dictn= {"john":"yes","wick":"yes","thor":"yes"}
        self.lst=["1","3","9"]
        
    
    def divide_or_square(self):
        if self.number%5==0:
            return f"sqrt of {self.number} is {sqrt(self.number)}"
        else:
            return f"remainder of {self.number} is {self.number%5}"
        
    def longest_value(self):
        a=self.divide_or_square()
        print(a)
        longest_name= max(self.dictonary.values(),key=len)
        return f"longest Value is:{longest_name}"
    def register_check(self):
        print("Parent register")
        count= list(self.dictn.values()).count("yes")
        return f"Parent-Present Student:{count}"

class DayTwo(dayone):
    def __init__(self,name):
        self.name=name
        print("child-1",self.name)
        super().__init__()
        
        print("cild",self.name)
    def convert_add(self):
        return f"sum of string Number-->{sum([int(i) for i in self.lst])}"
    def check_duplicate(self,list1):
        duplicate=set([l for l in list1 if list1.count(l)>1])
        return f'duplicate value is:{duplicate if duplicate else "No Duplicate"}'
    def register_check(self):
        super().register_check()
        print("Child register")
        # count= list(self.dictn.values()).count("yes")
        # return f"child-Present Student:{count}"

a=dayone()
print(a.divide_or_square())
print(a.longest_value())
print(a.register_check())
b=DayTwo("nirmal")
print(b.register_check())
print(b.convert_add())
print(b.check_duplicate(['apple','mango','apple','kiwi']))

# # class Calculator:
# #     def add(self, a, b):
# #         return a + b

# #     def add(self, a, b, c):
# #         return a + b + c

# #     def add(self, a, b, c, d):
# #         return a + b + c + d

# # # Create an instance of Calculator
# # calc = Calculator()

# # # Call the overloaded add() methods
# # #print(calc.add(1, 2))              # Output: Error - TypeError: add() missing 1 required positional argument: 'c'
# # #print(calc.add(1, 2, 3))           # Output: 6
# # print(calc.add(1, 2, 3, 4))        # Output: 10


# class GeekforGeeks:

# 	# default constructor
# 	def __init__(self,k):
# 		self.geek = "GeekforGeeks"
# 		self.cabine=k
# 		# print(self.geek)

# 	# a method for printing data members
# 	def print_Geek(self):
# 		print(self.geek)


# # creating object of the class
# obj = GeekforGeeks(11)
# obj.geek="ram"
# print(obj.cabine)

# # calling the instance method using the object obj
# obj.print_Geek()

# Python program to illustrate destructor

# class A:
# 	def __init__(self, bb):
# 		self.b = bb

# class B:
# 	def __init__(self):
# 		self.a = A(self)
# 	def __del__(self):
# 		print("die")

# def fun():
# 	b = B()

# fun()

# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         print(f"Initializing {self.name}")

#     def __del__(self):
#         print(f"Destroying {self.name}")

# # Create two instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# Delete one odf the objects
# del obj1

# Output:
# Initializing Object 1
# Initializing Object 2
# Destroying Object 1
print()
print("/n/n/n")


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)  # Call constructor of parent class A

    def addition(self):
        print("Calling A's addition method...")
        return super().addition()  # Call the addition method of parent class A without using its return value
        

# Creating instances of both classes and calling the addition method
obj_a = A(5, 10)
obj_b = B(7, 3)

print("Result from class A:", obj_a.addition())  # Output: Result from class A: 15
print("Result from class B:", obj_b.addition())  # Output: Result from class B: 10
print()
print("\n")

class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print("Addition from Parent:", result)
        return result


class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def addition(self):
        a= super().addition()  # Call the addition method of Parent without returning its value
        result = self.a + self.b + self.c
        
        return result,a


# Creating an instance of Child class and calling the addition method
obj_child = Child(5, 10, 15)
obj_parent=Parent(10,10)
print(obj_parent.addition())
print(obj_child.addition())


