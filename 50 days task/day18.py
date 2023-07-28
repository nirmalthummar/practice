###Task one
def any_number(*arg):
    # if not arg:
    #     return 0.0
    # total=sum(arg)/len(arg)
    # return total

##Second method

    total=0
    count=0
    for num in arg:
        if isinstance(num, (int, float)):
                total += num
                count += 1
    if count == 0:
        return None
    average = total / count
    return average

###third method (3 method)

    numbers = [num for num in arg if isinstance(num, (int, float))]
    if not numbers:
        return None
    average = sum(numbers) / len(numbers)
    return average

n=any_number(12,35,40,50.50,"k")
print(n)


#####Task 2 day-18

def add_reverse(list1, list2):
    if len(list1) != len(list2):
        return "The lists are not of equal lengths."

    result = []
    for num1, num2 in zip(list1, list2):
        result.append(num1 + num2)

    return list(reversed(result))

 #   Second Method 

    if len(list1) != len(list2):
        return "The lists are not of equal lengths."

    result = [sum(pair) for pair in zip(list1, list2)]
    return list(reversed(result))

  #  Third Method

    if len(list1) != len(list2):
        return "The lists are not of equal lengths."

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return list(reversed(result))

   # Fourth Method

    if len(list1) != len(list2):
        return "The lists are not of equal lengths."

    result = [list1[i] + list2[i] for i in range(len(list1))]
    return result[::-1]


list1 = [10, 12, 34]
list2 = [12, 56, 78]
result = add_reverse(list1, list2)
print(result)  # Output: [112, 22, 68]

list3 = [1, 2, 3, 4]
list4 = [10, 20, 30]
result = add_reverse(list3, list4)
print(result)  # Output: The lists are not of equal lengths.
