def sort_dutch_flag(arr, pivot=1):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return arr
arr = [0, 1, 2, 2, 1, 0, 0, 2, 1, 1]
sorted_arr = sort_dutch_flag(arr)
print(sorted_arr)