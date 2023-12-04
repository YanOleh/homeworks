class MyIter:
    def __init__(self, iterable, step=1):
        self.iterable = iterable
        self.step = step
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            result = self.iterable[self.index]
            self.index += self.step
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if isinstance(index, int):
            new_index = 0 if self.step > 0 else len(self.iterable) - 1
            new_index += index * self.step
            if 0 <= new_index < len(self.iterable):
                return self.iterable[new_index]
            else:
                raise IndexError("Index out of range")
        else:
            raise TypeError("Index must be an integer")

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_iter = MyIter(my_list)


for item in my_iter:
    print(item)

print(my_iter[0])
print(my_iter[1])
print(my_iter[2])
