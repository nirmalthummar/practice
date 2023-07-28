# def average_calories():
#     calories = []
#     while True:
#         user_input = input("Enter calories intake for the day (or 'done' to calculate average): ")
#         if user_input.lower() == 'done':
#             break
#         try:
#             calories.append(float(user_input))
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")

#     if len(calories) == 0:
#         return 0  # No calories entered

#     average = sum(calories) / len(calories)
#     return average

# average = average_calories()
# print("Average calories intake:", average)


# Task 2Extra Challenge : Create a Nested List


def nested_lists(*args):
    nested_list = list(args)
    return nested_list

# # Test case
# list1 = [1, 2, 3, 5]
# list2 = [1, 2, 3, 4]
# list3 = [1, 3, 4, 5]

# result = nested_lists(list1, list2, list3)
# print(result)  # Output: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]

