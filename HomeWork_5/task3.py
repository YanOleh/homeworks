string_list = list(input("Enter any string: "))

for i in range(5):
    print(''.join(random.sample(string_list, len(string_list))), end=', ')