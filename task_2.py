def binary_search(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if sorted_array[mid] < target:
            low = mid + 1
        elif sorted_array[mid] > target:
            high = mid - 1
        else:
            return iterations, sorted_array[mid]

    # Якщо елемент не знайдено, повертаємо "верхню межу"
    if high < 0:
        return iterations, sorted_array[0]
    elif low >= len(sorted_array):
        return iterations, None
    else:
        return iterations, sorted_array[low]

# TEST:
arr = [0.1, 0.5, 1.2, 1.7, 2.3, 3.0, 3.5, 4.1, 4.9, 5.5]
target = 3.1
iterations, upper_bound = binary_search(arr, target)
print("Iterations:", iterations)
print("Upper Bound:", upper_bound)
