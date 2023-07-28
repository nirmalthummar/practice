def find_words_with_vowels(input_string):
    words_with_vowels = []
    vowels = set('aeiou')

    for word in input_string.split():
        if any(char in vowels for char in word.lower()):
            words_with_vowels.append(word)

    return words_with_vowels

s= "you have no rhthym"
print(find_words_with_vowels(s))
