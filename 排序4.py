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