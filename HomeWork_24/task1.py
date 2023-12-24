class MyStack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def delete(self):
        if self.items:
            return self.items.pop()

def reverse_sequence(input_items):
    stack = MyStack()
    reverse = []
    for char in input_items:
        stack.push(char)
    print(stack.items)
    while stack.items:
        reverse.append(stack.delete())
    return reverse

print(reverse_sequence('123456789'))





