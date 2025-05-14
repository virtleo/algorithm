def counting_sort(arr):
    # 1. 找出数组中最大值和最小值
    max_val = max(arr)
    min_val = min(arr)
    # 2. 统计每个元素出现的次数
    count=[0]*(max_val-min_val+1)
    for i in arr:
        count[i-min_val]+=1
    # 3. 计算累计频率
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    # 4. 排序
    sorted_arr=[0]*len(arr)
    for i in arr:
        sorted_arr[count[i-min_val]-1]=i
        count[i-min_val]-=1

    return sorted_arr

# 测试
arr=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(counting_sort(arr)) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
