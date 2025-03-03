#选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))

# 希尔排序
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(shell_sort(arr))

# 计数排序
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result
arr = [64, 34, 25, 12, 22, 11, 90]
print(counting_sort(arr))