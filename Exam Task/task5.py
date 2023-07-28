def condition(lst):
    l=[]
    for i in lst:
        if i >500:
              break
        elif i%5==0:
              if i>150:
                    continue
              else:
                    l.append(i)
    return l


number=[12,75,150,180,145,525,50]
print(condition(number))

