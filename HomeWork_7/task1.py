some_sentence = input('Enter some sentence: ' ).replace(',', ' ').replace('.', ' ').lower().split()
some_dict = {i: some_sentence.count(i) for i in some_sentence}

print(some_dict)