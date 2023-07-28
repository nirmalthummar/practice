# # TASK 1
def middle_figure(a, b):
    combined_str = a + b
    combined_str = combined_str.replace(" ", "")  # Remove whitespaces
    length = len(combined_str)

    if length % 2 == 0:
        return "no middle figure"
    else:
        middle_index = length // 2
        return combined_str[middle_index]

# Test case
a = "make love"
b = "not wars"
result = middle_figure(a, b)
print(result)  # Output: 'e'


### # TASK 2

