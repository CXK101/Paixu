# 桶排序
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 创建桶
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    # 将元素分到桶中
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # 对每个桶进行排序
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])

    # 合并桶中的元素
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


# 示例
arr = [0.42, 0.32, 0.23, 0.57, 0.92, 0.34, 0.89]
print(bucket_sort(arr))
时间复杂度
分配元素：O(n)，遍历列表一次。
排序每个桶：假设每个桶中的元素数量为 m，则排序一个桶的时间复杂度为 O(m log m)。如果桶的数量为 k，则总时间复杂度为 O(k * m log m)。
合并桶：O(n)，遍历所有桶一次。
总时间复杂度：O(n + k * m log m)，其中 n 是列表长度，k 是桶的数量，m 是每个桶的平均元素数量。
空间复杂度
O(n + k)，需要额外的存储空间来存放桶和排序后的结果。
优缺点
优点：
当数据分布均匀时，性能优异。
适合外部排序（如对磁盘文件进行排序）。
缺点：
当数据分布不均匀时，某些桶中的元素数量过多，导致性能下降。
需要额外的存储空间。

# 组合排序
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3  # 步长收缩因子
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False

    return arr
# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print(comb_sort(arr))
时间复杂度：
最坏时间复杂度：O(n²) （虽然比冒泡排序稍好，但在最坏情况下与冒泡排序相同）
平均时间复杂度：O(n log n)（更快的情况下）
最佳时间复杂度：O(n)（当输入已经有序时）
空间复杂度：
空间复杂度：O(1)（因为它是原地排序算法，不需要额外的空间）
优点：
比冒泡排序更高效：由于使用了间隔减少的技巧，组合排序通常比普通的冒泡排序更有效。
简单易实现：实现相对简单，作为冒泡排序的改进版，代码实现非常直观。
原地排序：与冒泡排序一样，组合排序也是原地排序算法，不需要额外的空间。
缺点：
最坏情况复杂度仍然为O(n²)：尽管组合排序比冒泡排序更高效，但在最坏情况下，复杂度仍然是O(n²)，所以在数据规模非常大的情况下，可能表现不如快速排序或归并排序。
对小规模数据效果不明显：当数据规模较小，组合排序的优势可能不明显，因为其改进是基于较大规模数据的。
