# import random
# print("""
# **************************************************
#             Find Second Highest odd Number.  
# **************************************************
# """)

# # Value1 = int(input("Enter The Value : "))
# Value1 = 20

# list1 = []
# for i in range(1, Value1 + 1):
#     list1.append(random.randint(1, Value1))


# # ------------- Below Write Your code ---------- #


# print(f"Original List: {list1}")


# remove_duplicate_value = sorted(set(list1))
# print(f"\n\nremove_duplicate_value : {remove_duplicate_value}")

# new_list = []
# for i in remove_duplicate_value:
#     if i % 2 != 0:
#         new_list.append(i)
# print(f"Second Highest odd Number : {new_list[-2]}")




# # One line 
# second_highest_odd_number = [i for i in sorted(set(list1)) if i % 2 != 0][-2]
# print(f"\n\n Second Highest odd Number : {second_highest_odd_number}")




lst = [
{"value":1},{"value":3},{"value":0},{"value":4}
]

lst.sort()
print(lst)

