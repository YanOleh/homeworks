class MyStack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def delete(self):
        if self.items:
            return self.items.pop()

    def get_from_stack(self, element):
        for el in self.items:
            if el == element:
                return f'found_element: {self.items.pop(self.items.index(element))}'
        raise ValueError(f"Element '{element}' not found in the queue")


stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.items)
print(stack.get_from_stack(20))
print(stack.items)


class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.insert(0, element)

    def delete(self):
        if self.items:
            return self.items.pop()

    def get_from_stack(self, element):
        for el in self.items:
            if el == element:
                return f'found_element: {self.items.pop(self.items.index(element))}'
        raise ValueError(f"Element '{element}' not found in the queue")


queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
print(queue.items)
print(queue.get_from_stack(20))
print(queue.items)



