# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))
时间复杂度
最坏情况：O(n²)，当列表是逆序时，每次插入都需要移动所有已排序元素。
最好情况：O(n)，当列表已经有序时，只需遍历一次列表。
平均情况：O(n²)。
空间复杂度
O(1)，插入排序是原地排序算法，不需要额外的存储空间。
优缺点
优点：
实现简单，代码易于理解。
对小规模数据或基本有序的数据效率较高。
原地排序，不需要额外的存储空间。
稳定排序算法（相同元素的相对顺序不会改变）。
缺点：
时间复杂度较高，不适合大规模数据集。

# 基数排序
def radix_sort(arr):
    # 获取最大值的位数
    max_num = max(arr)
    exp = 1  # 从个位开始排序
    while max_num // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10
    return arr


def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 根据位数统计出现次数
    for num in arr:
        index = num // exp
        count[index % 10] += 1

    # 累加计数数组
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 排序
    for i in range(n - 1, -1, -1):
        num = arr[i]
        index = num // exp
        output[count[index % 10] - 1] = num
        count[index % 10] -= 1

    return output


# 示例
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))
时间复杂度
每一轮排序：O(n)，使用计数排序对每一位进行排序。
总轮数：k 轮，其中 k 是最大数字的位数。
总时间复杂度：O(n * k)。
空间复杂度
O(n + k)，需要额外的存储空间来存放计数数组和输出数组。
优缺点
优点：
时间复杂度为 O(n * k)，当 k 较小时，性能优异。
稳定排序算法（相同元素的相对顺序不会改变）。
缺点：
仅适用于整数或固定长度的字符串。
当最大数字的位数 k 很大时，性能下降。


# TimSort
def tim_sort(arr):
    return sorted(arr)

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print(tim_sort(arr))
时间复杂度：
最坏情况下时间复杂度：O(n log n)
平均情况下时间复杂度：O(n log n)
最佳情况下时间复杂度：O(n)（当输入已经部分或完全排序时，插入排序的性能可以达到线性）
Timsort的时间复杂度在最坏情况下类似于归并排序（O(n log n)），但在最佳情况下（已排序或几乎排序的数据），它会退化成 O(n)。
空间复杂度：
空间复杂度：O(n)
Timsort 需要额外的空间来存储临时数组，主要是在合并阶段。
优点：
高效性：在处理部分排序的数组时，Timsort 的表现比传统的排序算法（如快速排序和归并排序）更好。
稳定性：Timsort 是稳定的排序算法，即相等元素的相对顺序不会改变。
处理已排序部分的效率：对于已经部分排序或几乎有序的数据，Timsort 可以极大提高效率，使用插入排序来优化排序过程。
广泛应用：由于其稳定性和高效性，Timsort 被 Python 和 Java 等语言的标准库作为默认排序算法。
缺点：
空间消耗：与原地排序算法（如快速排序）相比，Timsort 需要额外的 O(n) 空间。
较复杂的实现：Timsort 比其他排序算法（如插入排序或快速排序）更复杂，需要管理许多边界情况和合并策略。
