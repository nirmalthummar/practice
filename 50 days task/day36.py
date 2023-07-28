def count(string):
    counts = {char: string.count(char) for char in string}
    return counts

string = "hello"
result = count(string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


#### SECONDDD WAYYYYY ######

from collections import Counter

def count(string):
    counts = Counter(string)
    #print("hello",counts)
    return dict(counts)


string = "hello"
result = count(string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


###### ##  THIRDDDD WAYYYYY ####### ####

def count(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

string = "hello"
result = count(string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


##### b##### FOURTH WAY #######


def count(string):
    return {char: string.count(char) for char in set(string)}


string = "hello"
result = count(string)
print(result)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

