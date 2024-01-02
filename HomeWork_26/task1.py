def binary_search(list1, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if list1[mid] == x:
            print(f'Number {x} found in position {mid}.')
            return True
        elif list1[mid] > x:
            return binary_search(list1, low, mid - 1, x)
        else:
            return binary_search(list1, mid + 1, high, x)
    else:
        print(f'Number {x} not found')
        return False


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(list1, 0, len(list1) - 1, 7)


def fibonacci_search(arr, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < x:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif arr[i] > x:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and arr[offset + 1] == x:
        return offset + 1

    return -1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 4
result = fibonacci_search(list1, 4)
print(f'Number {x} found in position {result}.')

