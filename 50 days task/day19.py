#####Task 1

def count_words(string):
    words = string.split()
    print(words)
    return len(words)

def count_elements(string):
    elements = len(string.replace(" ", ""))
    return elements


sentence = "I love learning"
word_count = count_words(sentence)
element_count = count_elements(sentence)
print(f"Word count: {word_count}")        
print(f"Element count: {element_count}")  

##Task 2 Extra Challenge