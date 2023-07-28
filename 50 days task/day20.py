# Task 1 Capitalize First Letter

# def capt(Capitalizes):
#     a = Capitalizes.title()
#     return a

# print(capt("i like learning"))
# s= "i love inDia"
# print(s.lower())

# task 2

def reverse_list(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words if any(letter.isupper() for letter in word)]
    return reversed_words
 
string = "HeLlo World I Love Python"
result = reverse_list(string)
print(result)  # Output: ['olleH', 'dlroW', 'I', 'evoL', 'nohtyP']


