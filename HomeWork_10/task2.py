def num_squared(a, b):
    result = int(a) ** 2 / int(b)
    return result


a, b = input("Enter first number: "), input("Enter second number: ")


def errors():
    try:
        print(num_squared(a, b))
    except ValueError:
        print("Oops! Value error. Try again...")
    except ZeroDivisionError:
        print("Oops! is not divisible by zero, Try again... ")

errors()