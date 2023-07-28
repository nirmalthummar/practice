def search_binary(lst, item):
    lst.sort()  # Sort the list in ascending order
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    # Item not found in the list
    return -1

# Test the function
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
item = 22
index = search_binary(list1, item)
print(f"Index of {item} in the list: {index}")
