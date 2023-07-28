def check_duplicates(lst):

    # duplicate_list = []
    # unique_list = []
    # for item in lst:
    #     if item in unique_list:
    #         duplicate_list.append(item)
    #     else:
    #         unique_list.append(item)
    # return duplicate_list if duplicate_list else "NO duplicate"

    duplicates = [l for l in lst if lst.count(l) > 1]
    return set(duplicates) if duplicates else "No duplicates"

fruits = ['apple', 'orange', 'banana', 'mango', 'banana', 'apple','kiwi','mango']
names = ['yamaha', 'hero', 'honda', 'suzuki']

print(check_duplicates(fruits))
print(check_duplicates(names))



