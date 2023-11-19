list1 = list(range(1, 101))
list2 = []

i = 0
while i < len(list1):
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        list2.append(list1[i])
    i += 1

print(list2)