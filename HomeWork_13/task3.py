nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums: list, func1, func2):
    if all(i > 0 for i in nums):
        return func1
    else:
        return func2

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

select_func = choose_func(nums1, square_nums, remove_negatives)
result = select_func(nums1)

print(result)
