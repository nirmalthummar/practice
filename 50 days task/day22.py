# def add_hash(string):
#     words = string.split()
#     modified_string = '#'.join(words)
#     print(words)  # Print the modified string
#     return modified_string

# def add_underscore(string):
#     modified_string = string.replace('#', '_')
#     print(modified_string)  # Print the modified string
#     return modified_string

# def remove_underscore(string):
#     modified_string = string.replace('_', '')
#     print(modified_string)  # Print the modified string
#     return modified_string

# result = remove_underscore(add_underscore(add_hash('Python')))
# print(result)  # Output: 'Python'


def add_hash(string):
    
    modified_string = '#'.join(string)
    print(modified_string)  # Print the modified string
    return modified_string

def add_underscore(string):
    modified_string = string.replace('#', '_')
    print(modified_string)  # Print the modified string
    return modified_string

def remove_underscore(string):
    modified_string = string.replace('_', '')
    print(modified_string)  # Print the modified string
    return modified_string

result = remove_underscore(add_underscore(add_hash('Python')))
print(result)  # Output: 'Python'


