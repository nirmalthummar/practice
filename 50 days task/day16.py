# Task one

# def sum_list(lst):
#     a= sum([j for i in lst for j in i])
#     return a

# l=[[2,4,5,6],[2,3,5,6]]
# print(sum_list(l))

# task 2

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
numbers = [34, 67, 78]

output_list = []

for sublist in nested_list:
    for number in sublist:
        if number in numbers and number not in output_list:
            output_list.append(number)

print(output_list)
