# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))

# 堆排序
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # 转换成最小堆
    return [heapq.heappop(arr) for _ in range(len(arr))]
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))