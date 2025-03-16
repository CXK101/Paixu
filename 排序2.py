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
时间复杂度
最坏情况：O(n²)，无论输入数据是否有序，都需要进行 n(n-1)/2 次比较。
最好情况：O(n²)，即使列表已经有序，仍需进行相同数量的比较。
平均情况：O(n²)。
空间复杂度
O(1)，选择排序是原地排序算法，不需要额外的存储空间。
优缺点
优点：
实现简单，代码易于理解。
原地排序，不需要额外的存储空间。
对于小规模数据集，性能尚可接受。
缺点：
时间复杂度较高，不适合大规模数据集。
不稳定排序算法（如果存在相同元素，可能会改变它们的相对顺序）。



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
时间复杂度
希尔排序的时间复杂度取决于增量序列的选择：
最坏情况：O(n²)，当增量序列选择不当时。
最好情况：O(n log n)，当增量序列选择合适时。
平均情况：O(n log n) 到 O(n²) 之间。
常见的增量序列：
希尔增量：n/2, n/4, ..., 1，时间复杂度为 O(n²)。
Hibbard 增量：1, 3, 7, 15, ..., 2^k - 1，时间复杂度为 O(n^(3/2))。
Sedgewick 增量：1, 5, 19, 41, 109, ...，时间复杂度为 O(n^(4/3))。
空间复杂度
O(1)，希尔排序是原地排序算法，不需要额外的存储空间。
优缺点
优点：
相对于简单插入排序，效率更高。
原地排序，不需要额外的存储空间。
适用于中等规模的数据集。
缺点：
时间复杂度依赖于增量序列的选择。
不稳定排序算法（可能改变相同元素的相对顺序）。

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
时间复杂度
统计频率：O(n)，遍历列表一次。
累加频率：O(k)，遍历计数数组一次。
放置元素：O(n)，遍历列表一次。
总时间复杂度：O(n + k)，其中 n 是列表长度，k 是数据的范围大小。
空间复杂度
O(n + k)，需要额外的计数数组和结果数组。
优缺点
优点：
时间复杂度为 O(n + k)，当 k 较小时，性能优异。
稳定排序算法（相同元素的相对顺序不会改变）。
缺点：
仅适用于整数或有限范围内的数据。
当数据范围 k 很大时，空间复杂度较高。
