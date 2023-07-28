### TASK 1 #### ##

def inter_section(list1, list2):
    intersection = tuple([num for num in list1 if num in list2])
    return intersection

# Test the function
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
result = inter_section(list1, list2)
print(result)


##### TASK 2  ##### #

import timeit

# Create the range
a = range(10000000)

# Convert range to set and list
x = set(a)
y = list(a)

# Define the number to search for
number = 9999999

# Measure the time taken to search in the set
set_time = timeit.timeit(lambda: number in x, number=1)

# Measure the time taken to search in the list
list_time = timeit.timeit(lambda: number in y, number=1)

# Compare the times
if set_time < list_time:
    print("Searching in the set is faster.")
else:
    print("Searching in the list is faster.")
