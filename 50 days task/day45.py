def analyse_string(string):
    special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_count = sum(string.count(char) for char in special_characters)
    word_count = len(string.split())
    total_characters = len(string.replace(" ", ""))

    analysis = {
        "special characters": special_count,
        "words": word_count,
        "total characters": total_characters
    }

    return analysis

# Test the function
string = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. \"spam=%s eggs=%d\" % (\"blah\", 2) evaluates to \"spam=blah eggs=2\". source wikipidia"
result = analyse_string(string)
print(result)
