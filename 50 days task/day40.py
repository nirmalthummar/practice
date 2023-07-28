def translate(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    translated_words = []

    for word in words.split():
        if word[0].lower() in vowels:
            translated_words.append(word + 'yay')
        else:
            translated_words.append(word[1:] + word[0] + 'ay')

    return ' '.join(translated_words)

# Example usage
a = 'we love python'
translation = translate(a)
print(translation)
