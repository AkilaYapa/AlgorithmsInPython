arr = [3, 7, 1, 5, 9, 2]
print("Original array:")
print(arr)


# Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        for j in range(i - 1, -1, -1):
            if num < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = num
    return arr


result_insertion = insertion_sort(arr)
print("Insertion sort :")
print(result_insertion)


# selection sort

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


print("Selection Sort :")
print(selection_sort(arr))


# bubble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("Bubble sort :")
print(bubble_sort(arr))
