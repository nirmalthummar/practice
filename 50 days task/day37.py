#### FIRST WAY ####

def count_the_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

string = "hello"
result = count_the_vowels(string)
print(result)  # Output: 2


#####  #### SECOND WAYYYY #######

def count_the_vowels(string):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in string if char in vowels)
    return count

string = "hello"
result = count_the_vowels(string)
print(result)  # Output: 2


#### ### THIRD WAY ###### ### 

def count_the_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

string = "hello"
result = count_the_vowels(string)
print(result)  # Output: 2


#### FORTH WAYYYY ######

def count_the_vowels(string):
    vowels = 'aeiouAEIOU'
    count = len([char for char in string if char in vowels])

    return count


string = "hello"
result = count_the_vowels(string)
print(result)  # Output: 2
