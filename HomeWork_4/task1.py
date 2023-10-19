word = input('Enter any word: ')

if len(word) >= 2:
    print(word[:2], word[-2:], sep='')
else:
    print('Empty String')
