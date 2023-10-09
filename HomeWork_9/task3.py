def make_operation(operator, *args):
    return_value = 0

    if operator == '+':
        for num in args:
            return_value += num
    elif operator == '-':
        if len(args) >= 2:
            return_value = args[0]
            for num in args[1:]:
                return_value -= num
        else:
            return_value = args[0]
    elif operator == '*':
        return_value = 1
        for num in args:
            return_value *= num
    return return_value

print(make_operation('*',6,7))
print(make_operation('+',7,7,2))
print(make_operation('-',5,5,-10,-20))