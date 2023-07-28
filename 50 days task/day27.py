### # TASK 1

# # FIRST WAY

# def unique_numbers(numbers):
#     unique_nums = set(numbers)
#     sum_all = sum(numbers)
#     sum_unique = sum(unique_nums)
#     difference = sum_all - sum_unique

#     if difference % 2 == 0:
#         return numbers
#     else:
#         return list(unique_nums)

# # Test case
# numbers = [1, 2, 4, 5, 6, 7, 8, 8]
# result = unique_numbers(numbers)
# print(result)  # Output: [1, 2, 4, 5, 6, 7, 8, 8]

# ## # SECOND WAY TO SOLVE ####

# def unique_numbers(numbers):
#     unique_nums = [num for num in numbers if numbers.count(num) == 1]
#     sum_all = sum(numbers)
#     sum_unique = sum(unique_nums)
#     difference = sum_all - sum_unique

#     if difference % 2 == 0:
#         return numbers
#     else:
#         return unique_nums

# # Test case
# numbers = [1, 2, 4, 5, 6, 7, 8, 8]
# result = unique_numbers(numbers)
# print(result)  # Output: [1, 2, 4, 5, 6, 7, 8, 8]

# ### ## ## # Task 2 # ## ## ###

# def difference(list1, list2):
#     diff_a = [elem for elem in list1 if elem not in list2]
#     diff_b = [elem for elem in list2 if elem not in list1]
#     return diff_a + diff_b

# # Test case
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# result = difference(list1, list2)
# print(result)  # Output: [4, 6, 7, 9]

## # Second WAY ## #


