
#### ### TASKKKK 11111 ###### ###

import random

def guess_a_number():
    number_to_guess = random.randint(1, 10)
    max_guesses = 3
    guess_count = 0

    while guess_count < max_guesses:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return

        guess_count += 1

    print("Sorry, you didn't guess the number. You lose.")

# Call the function
guess_a_number()


#####B #### TASK 2 ##### #####

def missing_numbers(sequence):
    min_num = min(sequence)
    max_num = max(sequence)
    all_numbers = set(range(min_num, max_num + 1))
    missing_numbers = all_numbers - set(sequence)
    missing_numbers = sorted(missing_numbers)
    return missing_numbers

# Example usage
sequence = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
missing_nums = missing_numbers(sequence)
print(missing_nums)


##### SECOND WAYYYYY #####

def missing_numbers(sequence):
    min_num = min(sequence)
    max_num = max(sequence)
    missing_numbers = [num for num in range(min_num, max_num + 1) if num not in sequence]
    return missing_numbers

# Example usage
sequence = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
missing_nums = missing_numbers(sequence)
print(missing_nums)
