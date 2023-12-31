''' task1 - Сделал с помощью чата gpt, потом по строчкам разобрался что к чему,
сам долго сидел и как-то не получалось '''

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

    def __repr__(self):
        return str(self._data)


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(temp)

    def index(self, item):
        current = self._head
        position = 0
        while current is not None:
            if current.get_data() == item:
                return position
            else:
                current = current.get_next()
                position += 1
        raise ValueError(f"{item} not in list")

    def pop(self, index=None):
        if index is None:
            index = self.size() - 1

        if index < 0 or index >= self.size():
            raise IndexError("pop index out of range")

        current = self._head
        previous = None
        position = 0

        while position < index:
            previous = current
            current = current.get_next()
            position += 1

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def insert(self, index, data):
        temp = Node(data)
        if index == 0:
            temp.set_next(self._head)
            self._head = temp
        else:
            current = self._head
            i = 0
            while i != index - 1:
                i += 1
                current = current.get_next()
            temp.set_next(current.get_next())
            current.set_next(temp)

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __getitem__(self, index):
        current = self._head
        i = 0
        while i != index:
            current = current.get_next()
            i += 1
        return current.get_data()

    def slice(self, start, stop):
        current_node = self._head
        result = []
        if self._head is None:
            raise ValueError("List is empty")
        if start or stop > self.size():
            raise ValueError("Out of Range")
        i = 0
        while i < start:
            current_node = current_node.get_next()
            i += 1
        while i < stop:
            result.append(current_node.get_data())
            current_node = current_node.get_next()
            i += 1
        return result


if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))