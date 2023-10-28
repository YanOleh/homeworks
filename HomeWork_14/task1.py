def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called {args}")
        result = func(*args)
        return result
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))