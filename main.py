def insertion_sort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        for j in range(i - 1, -1, -1):
            if num < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = num
    return arr


arr = [3, 5, 1, 7, 9, 5, 3, 8]

result = insertion_sort(arr)
print(result)
