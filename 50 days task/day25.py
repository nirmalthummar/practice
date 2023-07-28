# Task 1

# def all_the_same(elements):
#     return all(element == elements[0] for element in elements)

# # Test cases
# list1 = ['Mary', 'Mary', 'Mary']
# print(all_the_same(list1))  # Output: True

# list2 = ['Mary', 'John', 'Mary']
# print(all_the_same(list2))  # Output: False

# string1 = "Hello"
# print(all_the_same(string1))  # Output: False

# string2 = "aaa"
# print(all_the_same(string2))  # Output: True

# tuple1 = (1, 1, 1)
# print(all_the_same(tuple1))  # Output: True


# def all_the_same(elements):
#     return len(set(elements)) == 1

# # Test cases
# list1 = ['Mary', 'Mary', 'Mary']
# print(all_the_same(list1))  # Output: True

# list2 = ['Mary', 'John', 'Mary']
# print(all_the_same(list2))  # Output: False

# string1 = "Hello"
# print(all_the_same(string1))  # Output: False

# string2 = "aaa"
# print(all_the_same(string2))  # Output: True

# tuple1 = (1, 1, 1)
# print(all_the_same(tuple1))  # Output: True

# def all_the_same(elements):
#     return elements.count("") == len(elements)

# # Test cases
# list1 = ['Mary', 'Mary', 'Mary']
# print(all_the_same(list1))  # Output: True

# list2 = ['Mary', 'John', 'Mary']
# print(all_the_same(list2))  # Output: False

# string1 = "Hello"
# print(all_the_same(string1))  # Output: False

# string2 = "aaa"
# print(all_the_same(string2))  # Output: True

# tuple1 = (1, 1, 1)
# print(all_the_same(tuple1))  # Output: True


# def all_the_same(elements):
#     return not any(element != elements[0] for element in elements[1:])

# # Test cases
# list1 = ['Mary', 'Mary', 'Mary']
# print(all_the_same(list1))  # Output: True

# list2 = ['Mary', 'John', 'Mary']
# print(all_the_same(list2))  # Output: False

# string1 = "Hello"
# print(all_the_same(string1))  # Output: False

# string2 = "aaa"
# print(all_the_same(string2))  # Output: True

# tuple1 = (1, 1, 1)
# print(all_the_same(tuple1))  # Output: True

## Task 2 eXTRA Challenge
# #TASK 2
# # Task 2


# def read_backwards(str1):
#     words = str1.split()
#     reversed_str = ' '.join(words[::-1])
#     return reversed_str

# # Test case
# str1 = "the love is real"
# result = read_backwards(str1)
# print(result)  # Output: "laer si evol eht"
