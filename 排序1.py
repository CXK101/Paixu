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
时间复杂度
最坏情况：O(n²)，当列表是逆序时。
最好情况：O(n)，当列表已经有序时。
平均情况：O(n²)。
空间复杂度
O(1)，因为冒泡排序是原地排序算法，不需要额外的存储空间。
优缺点
优点：
实现简单，代码易于理解。
原地排序，不需要额外的存储空间。
缺点：
效率较低，尤其是对于大规模数据集。
不适合处理几乎已经有序的列表，因为仍然需要进行多次遍历。



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
时间复杂度
分解：每次将列表分成两半，需要 O(log n) 层递归。
合并：每层递归需要 O(n) 的时间来合并子列表。
总时间复杂度：O(n log n)。
空间复杂度
O(n)，归并排序需要额外的空间来存储临时列表。
优缺点
优点：
时间复杂度稳定为 O(n log n)，适合大规模数据。
稳定排序算法（相同元素的相对顺序不会改变）。
适合外部排序（如对磁盘文件进行排序）。
缺点：
需要额外的存储空间，空间复杂度为 O(n)。
对于小规模数据，性能可能不如插入排序等简单算法。

# 堆排序
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # 转换成最小堆
    return [heapq.heappop(arr) for _ in range(len(arr))]
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))
时间复杂度
构建最大堆：O(n)。
每次调整堆：O(log n)，总共需要调整 n-1 次。
总时间复杂度：O(n log n)。
空间复杂度
O(1)，堆排序是原地排序算法，不需要额外的存储空间。
优缺点
优点：
时间复杂度稳定为 O(n log n)，适合大规模数据。
原地排序，不需要额外的存储空间。
缺点：
不稳定排序算法（可能改变相同元素的相对顺序）。
对于小规模数据，性能可能不如插入排序等简单算法。
