def in_range(start, end, step=2):
    current_value = start
    while (step > 0 and current_value < end) or (step < 0 and current_value > end):
        yield current_value
        current_value += step

# Example usage:
for i in in_range(10, 1, -1):
    print(i)
