def with_index(iterable, start=0):
    current_index = start
    for element in iterable:
        yield current_index, element
        current_index += 1

# Example usage:
fruits = ['a', 'b', 'c']

for index, value in with_index(fruits, 1):
    print(f"Index: {index}, Value: {value}")


for index, value in enumerate(fruits):
    print(index, value)