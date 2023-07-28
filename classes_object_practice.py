# A Python program to demonstrate inheritance
"""class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()


class Emp(Person):

    def Print(self):
        print("Emp class called")
        
Emp_details = Emp("Mayank", 103)"""

# calling parent class function
#Emp_details.Display()

# Calling child class function
#Emp_details.Print()


#######################################################
print("\n \n")
#########################################################


"""class A:
	def __init__(self, n='Rahul'):
		self.name = n

class B(A):
	def __init__(self, roll):
              super().__init__()
              self.roll = roll
                
        

object = B(23)
print(object.name)
print()"""


""" GLOBAL KEYWORD"""
"""

x=15
print("x =",x)

def change():
      
      global x

      x = x+5
      print("value of x inside a function :",x)
      
change()
print("value of x outside a function",x)

# OUTPUT IS
# x = 15
# value of x inside a function : 20
# value of x outside a function 20

"""
# #print("hello","ram",sep=" 456 ")
# #print("world")

# #name= "n i r m a l"
## print("name=",name)
# #b=name.split(" ")
# #print("b=",len(b))
# #print("b=",b)
# #a="-".join(b)
# #print("a=",len(a))

# #print("a",a)

## Using dir() and len() to count the number of built-in functions
# #num_builtin_functions = dir(__builtins__)
# #print("Total number of built-in functions in Python:", num_builtin_functions)
# #c=dir()
# #print("c=================================",c)


"""
# original_string = 1,2,3
# b=str(original_string)
# print(b[0])
# print(type(b))"""

"""s="hello to Nirmal"
a=s.capitalize()
print(a)"""

## OUTPUT :: Hello to nirmal

"""s="hello TO NIRMAL"
b=s.casefold()
print(b)"""

## output is===== hello to nirmal
"""
#s="NIR"
#b=s.center(10)
#print(b," ",len(b))"""

### "   NIR    "   10

"""
As you can see, the string "NIR" is centered
 with 4 spaces on the left side and 3 spaces on the right
side within a total width of 10 characters.
The total length of the resulting string is 10, 
which includes the original
string "NIR" and the extra spaces added for centering.
"""

"""s="hello TO NIRMAL"
if s.endswith("L"):
      print("hello")

# Example using rsplit()
sentence = "Hello, how are you?"
words = sentence.rsplit()  # If no separator is provided, rsplit() uses whitespace as the default separator.
print(words)
# Output: ['Hello,', 'how', 'are', 'you?']
l1=[1,2,3,4]
l2=["hello","student","k"]
l1.extend(l2)
print(l1)
l1.reverse()
print(l1)
b=l2.count("hello")
print(b)
c=l2.pop()
print(l2)
l2.remove("hello")
print(l2)
l=["a","b","c","d","e"]
n=l[-5:-4]
print(n)

l.clear()

f={3,2,7}
g={9,2,6,4}
f.update(range(8))
print(f)"""
"""
def find_common_letters(strings):
    if not strings:
        return []

    # Convert each string to a set of its unique characters
    sets_of_letters = [set(s) for s in strings]
    print("sets_of_letters====",sets_of_letters)

    # Calculate the intersection of all sets
    common_letters = set.intersection(*sets_of_letters)

    return list(common_letters)

# Example usage:
l = ["ahmedabad", "mumbai", "baroda"]
result = find_common_letters(l)
print(result)  # Output: ['a', 'b']

"""

"""def find_common_letters(strings):
    if not strings:
        return []

    # Convert the first string into a set of its unique characters
    common_letters = set(strings[0])

    # Find the intersection with the sets of the remaining strings
    for s in strings[1:]:
        common_letters &= set(s)

    return list(common_letters)

# Example usage:
l = ["ahmedabad", "mumbai", "baroda"]
result = find_common_letters(l)
print(result)  # Output: ['a', 'b']"""
"""
l1=[1,2,3]
l2=[2,3,4]
set1=set(l1)
set2=set(l2)
l3=list(set1.difference(set2))
print(l3)"""

"""set1={1,2,3}
l=[{3,4,5},{3,8,9}]

a=set1.intersection(*l)
print(a)"""

# s={1,2,3,4,5,6,7,8}
# s.remove(3)
# print(s)

# Python code to demonstrate how parent constructors
# are called.

# parent class
"""class Person():

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber
		

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self,name,idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()"""

class A:
	def __init__(self, n):
		self.name = n

class B(A):
	def __init__(self, roll,l):
		self.roll = roll
		super().__init__()

object = B(2,5)
print(object.name)


# parent class
class Person():
    def __init__(self,age ,name):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        # inheriting the properties of parent class
        super().__init__("rahul", age)

    def displayInfo(self):
        print(self.name, self.age)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()





