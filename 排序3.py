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

# TimSort
def tim_sort(arr):
    return sorted(arr)

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print(tim_sort(arr))
