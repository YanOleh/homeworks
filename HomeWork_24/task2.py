class MyStack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def delete(self):
        if self.items:
            return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        elif len(self.items) > 0:
            return False


def balanced(input_items):
    stack = MyStack()
    balance = True
    index = 0
    open = "([{"
    close = ")]}"
    while index < len(input_items) and balance:
        symbol = input_items[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balance = False
            else:
                top = stack.delete()
                if open.index(top) != close.index(symbol):
                    balance = False
        index += 1
    if balance and stack.is_empty():
        return "balance"
    else:
        return "not balance"


balance_str = '(()())[][]'
not_balance_str = '[[[]{{}'

print(balanced(balance_str))
print(balanced(not_balance_str))










