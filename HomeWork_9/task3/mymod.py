def count_lines(name):
    with open(name, 'r') as my_text:
        return len(my_text.readlines())

def count_chars(name):
    with open(name, 'r') as my_text:
        return len(my_text.read().replace('\n', ''))

def test(name):
    return count_lines(name), count_chars(name)


name = input()


print(count_lines(name))
print()
print(count_chars(name))
print()
print(test(name))