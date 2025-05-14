def insertion_sort(arr):
    length=len(arr)
    for i in range(1,length):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([12,4,55,65,7457,636,346,357]))
        