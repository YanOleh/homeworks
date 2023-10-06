import random

list1 = []
list2 = []
list3 = []


while True:
    list1.append(random.randint(1,10))
    list2.append(random.randint(1,10))
    if len(list2) == 10:
        break

for i in list1:
    if i in list2:
        list3.append(i)

print('List1 =', list1, '\n' 'List2 =', list2, '\n' 'List3 =', list(set(list3)))