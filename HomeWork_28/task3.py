import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        arr[:] = quicksort(left) + middle + quicksort(right)
    return arr


random_list = [random.randint(0, 100) for _ in range(20)]
print("Before sorted:", random_list)
sorted_list = quicksort(random_list)
print("After sorted:", sorted_list)
