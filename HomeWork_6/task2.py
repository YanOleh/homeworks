import random

list1 = []
list2 = []
list3 = []


while True:
    list1.append(random.randint(1,10))
    list2.append(random.randint(1,10))
    if len(list2) == 10:
        break

list3 = list(set(list1) & set(list2))


print('List1 =', list1, '\n' 'List2 =', list2, '\n' 'List3 =', list3)