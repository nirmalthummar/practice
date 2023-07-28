def check_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()

    for char in alphabet:
        if char not in sentence:
            return False

    return True

sentence = 'the quick brown fox jumps over a lazy dog'
result = check_pangram(sentence)
print(result)  # Output: True



#### second way #####

def check_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()
    sentence_chars = set(sentence.replace(' ', ''))

    return alphabet == sentence_chars


sentence = 'the quick brown fox jumps over a lazy dog'
result = check_pangram(sentence)
print(result)  # Output: True


###### ## # THIRD WAY ### ### #

def check_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()

    return all(char in sentence for char in alphabet)


sentence = 'the quick brown fox jumps over a lazy dog'
result = check_pangram(sentence)
print(result)  # Output: True


#### ## ## FORTH WAY #######


def check_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = sentence.lower()

    return alphabet.issubset(sentence)

sentence = 'the quick brown fox jumps over a lazy dog'
result = check_pangram(sentence)
print(result)  # Output: True


##### TASK 2 #####

def find_index(lst, integer):
    if integer in lst:
        return [i for i, num in enumerate(lst) if num == integer]
    else:
        return [integer] * len(lst)


lst = [1, 2, 4, 6, 7, 7]
integer = 7
result = find_index(lst, integer)
print(result)  # Output: [4, 5]

lst = [1, 2, 4, 6, 7, 7]
integer = 8
result = find_index(lst, integer)
print(result)  # Output: [8, 8, 8, 8, 8, 8]


##### SECOND WAYYY #####

def find_index(lst, integer):
    indexes = []
    
    if integer in lst:
        for i in range(len(lst)):
            if lst[i] == integer:
                indexes.append(i)
    else:
        indexes = [integer] * len(lst)
    
    return indexes

lst = [1, 2, 4, 6, 7, 7]
integer = 7
result = find_index(lst, integer)
print(result)  # Output: [4, 5]

lst = [1, 2, 4, 6, 7, 7]
integer = 8
result = find_index(lst, integer)
print(result)  # Output: [8, 8, 8, 8, 8, 8]


###### ##  THIRDDD WAYYYY ##### ##


def find_index(lst, integer):
    indexes = [index for index, value in enumerate(lst) if value == integer]
    return indexes if indexes else [integer] * len(lst)


lst = [1, 2, 4, 6, 7, 7]
integer = 7
result = find_index(lst, integer)
print(result)  # Output: [4, 5]

lst = [1, 2, 4, 6, 7, 7]
integer = 8
result = find_index(lst, integer)
print(result)  # Output: [8, 8, 8, 8, 8, 8]


##### ### FOURTHHHH WAYYYY #### ###


def find_index(lst, integer):
    indexes = []
    for index, value in enumerate(lst):
        if value == integer:
            indexes.append(index)
    return indexes if indexes else [integer] * len(lst)


lst = [1, 2, 4, 6, 7, 7]
integer = 7
result = find_index(lst, integer)
print(result)  # Output: [4, 5]

lst = [1, 2, 4, 6, 7, 7]
integer = 8
result = find_index(lst, integer)
print(result)  # Output: [8, 8, 8, 8, 8, 8]
