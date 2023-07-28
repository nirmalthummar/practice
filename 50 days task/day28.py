## # TASK 1

def index_position(string):
    positions = [index for index, char in enumerate(string) if char.islower()]
    return positions

# Test case
string = 'LovE'
result = index_position(string)
print(result)  # Output: [1, 2]
"""
The enumerate() function is a built-in function 
in Python that allows you to iterate over a 
sequence while keeping track of the index of each element. 
It returns pairs of index and value, 
which can be unpacked into separate 
variables (in this case, index and char). 
This allows you to access both the index and 
value of each element 
in the iteration.

In the given implementation, enumerate(string) 
generates pairs of index and character 
for each character in the string. 
The for loop iterates over these pairs, 
allowing you to access the index 
and character in each iteration.

"""

### # SECOND WAY ### ##

def index_position(string):
    positions = [index if char.islower() else None for index, char in enumerate(string)]
    positions = [index for index in positions if index is not None]
    return positions

# Test case
string = 'LovETo'
result = index_position(string)
print(result)  # Output: [1, 2]

### # THIRD WAY ### ## #

def index_position(string):
    positions = []
    for index in range(len(string)):
        if string[index].islower():
            positions.append(index)
    return positions

# Test case
string = 'LovE'
result = index_position(string)
print(result)  # Output: [1, 2]

### # FOURTH WAY #### ## #
def index_position(string):
    positions = [i for i in range(len(string)) if string[i].islower()]
    return positions

# Test case
string = 'LovE'
result = index_position(string)
print(result)  # Output: [1, 2]


### FIFTH WAY TO SOLVE ### ## #

def index_position(string):
    positions = [pos for pos, char in zip(range(len(string)), string) if char.islower()]
    return positions

# Test case
string = 'LovE'
result = index_position(string)
print(result)  # Output: [1, 2]

### TASK 2 ###

def largest_number(nums):
    combined_num = ''.join(str(num) for num in nums)
    sorted_num = sorted(combined_num, reverse=True)
    print(sorted_num)
    largest_num = ''.join(sorted_num)
    formatted_num = "{:,}".format(int(largest_num))
    return formatted_num

# Test case
list1 = [3, 67, 87, 9, 2]
result = largest_number(list1)
print(result)  # Output: 9,877,632




