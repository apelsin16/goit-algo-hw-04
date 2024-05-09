import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate a large random array for testing
arr = [random.randint(0, 1000) for _ in range(1000)]

# Measure time for Merge Sort
merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=100)
print("Merge Sort time:", merge_sort_time)

# Measure time for Insertion Sort
insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=100)
print("Insertion Sort time:", insertion_sort_time)

# Measure time for Timsort (Python's built-in sorting algorithm)
timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=100)
print("Timsort time:", timsort_time)
