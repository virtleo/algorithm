def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):#n-1指默认最小值到倒数第二个元素
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(selection_sort([12,4,55,65,7457,636,346,357]))