import random

n = 0
list_number = []

while n < 10:
    random_number = random.randint(1,9)
    list_number.append(random_number)
    n += 1


print('List of random numbers:', list_number, '\n' 'Largest number:', max(list_number))