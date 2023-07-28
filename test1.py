

import random
Value1 = int(input("Enter The Value : "))
# Value1 = 10

list1 = []
for i in range(1, Value1 + 1):
    list1.append(random.randint(1, Value1))


# ------------- Write Your code ---------- #




print("""
******************************************************
                    Long Code 
******************************************************
""")

from datetime import datetime
startTime = datetime.now()
print(f"Start Time : {startTime}")


Odd_list = []

for i in list1:
    if i % 2 != 0:
        Odd_list.append(i)

removeDUplicate = set(Odd_list)
sortedList = sorted(removeDUplicate)

secondHighest  = sortedList[-2]

print(secondHighest)

endTime = datetime.now()

print(f"End Time : {datetime.now()}")
print(f"Total Time : {endTime-startTime}")



print("""
******************************************************
                    Short Code 
******************************************************
""")

from datetime import datetime
startTime = datetime.now()
print(f"Start Time : {startTime}")


Odd_list = sorted(set([i for i in list1 if i % 2 != 0]))[-2]

print(Odd_list)

endTime = datetime.now()

print(f"End Time : {datetime.now()}")
print(f"Total Time : {endTime-startTime}")

