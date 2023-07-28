# ## ### TASK 1 ### ## #

def longest_word(words):
    longest = ''
    longest_length = 0

    for word in words:
        if len(word) > longest_length:
            longest = word
            longest_length = len(word)

    return [longest_length, longest]

# Test the function
word_list = ['Java', 'JavaScript', 'Python']
result = longest_word(word_list)
print(result)


### ## # SECOND WAY #### ### ##


def longest_word(words):
    longest_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_length]
    return [longest_length, longest_words[0]]

# Test the function
word_list = ['Java', 'JavaScript', 'Python']
result = longest_word(word_list)
print(result)


### ## # THIRD WAY # ## ###


def longest_word(words):
    longest = max(words, key=len)
    longest_length = len(longest)
    return [longest_length, longest]

# Test the function
word_list = ['Java', 'JavaScript', 'Python']
result = longest_word(word_list)
print(result)


### ## # FOURTH WAY # ## ###


def longest_word(words):
    longest_length = 0
    longest_words = []

    for word in words:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length
            longest_words = [word]
        elif word_length == longest_length:
            longest_words.append(word)

    return [longest_length, longest_words[0]]

# Test the function
word_list = ['Java', 'JavaScript', 'Python']
result = longest_word(word_list)
print(result)


##### #### ### ## # TASK 2 # ## ### #### #####


def create_user():
    user_data = {}

    # Get user information
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")

    # Save user information in dictionary
    user_data['name'] = name
    user_data['age'] = age
    user_data['password'] = password

    print("User saved. Please login")

    # Login process
    while True:
        # Get login details
        login_name = input("Enter your name: ")
        login_password = input("Enter your password: ")

        # Check if login details match
        if login_name == user_data['name'] and login_password == user_data['password']:
            return "Logged in successfully"
        else:
            print("Wrong password or user name. Please try again")

# Test the function
result = create_user()
print(result)
