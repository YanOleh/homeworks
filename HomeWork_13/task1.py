def function():
    a = 10
    b = "Hello, World"
    c = 20

def count_local_var(func):
    local_variables = func.__code__.co_varnames
    return len(local_variables)

print(count_local_var(function))