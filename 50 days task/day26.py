 ## task 1

def sort_words(words):
    letters = sorted(set(words.replace(' ', '')))
    return [','.join(letters)]

# Test case
words = 'love life'
result = sort_words(words)
print(result)  # Output: ['e,f,i,l,o,v']


### # Second Way to solve problem

def sort_words(words):
    letters = sorted(set(char for char in words if char != ' '))
    return [','.join(letters)]


words = 'love life'
result = sort_words(words)
print(result)  

### # Third Way to solve

def sort_words(words):
    letters = sorted(set(''.join(words.split())))
    return [','.join(letters)]

# Test case
words = 'love life'
result = sort_words(words)
print(result)  # Output: ['e,f,i,l,o,v']

## # TASK 2

# #d={}
# #s="HI my name is Nirmal"
## a= s.split()
# #for i in range(len(a)):
# #    d[a[i]]=len(a[i])

## print(d)

### # First Way to solve this

# def string_length(words):
#     word_lengths = {}
#     word_list = words.split()
#     for word in word_list:
#         word_lengths[word] = len(word)
#     return word_lengths

# # Test case
# words = 'Hi my name is Richard'
# result = string_length(words)
# print(result)  # Output: {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}

# ## # SECOND WAY

# def string_length(words):
#     word_list = words.split()
#     word_lengths = {word: len(word) for word in word_list}
#     return word_lengths

# # Test case
# words = 'Hi my name is Richard'
# result = string_length(words)
# print(result)  # Output: {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}


# ## # THIRD WAY

# def string_length(words):
#     word_list = words.split()
#     word_lengths = dict(map(lambda word: (word, len(word)), word_list))
#     return word_lengths

# # Test case
# words = 'Hi my name is Richard'
# result = string_length(words)
# print(result)  # Output: {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
