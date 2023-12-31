class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def is_empty(self):
        return self.head is None


stack = StackLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
