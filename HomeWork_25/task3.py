class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        dequeued = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued

    def is_empty(self):
        return self.head is None


queue = QueueLinkedList()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.pop())
