import random
def quick_sort(arr):
    if len (arr)<2:
        return arr
    else:
        pivot=arr[0]
        left=[]
        right=[]
        for i in range(1,len(arr)):
            if arr[i]<pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left)+[pivot]+quick_sort(right)

# 随机化快速排序
def randomized_quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=random.choice(arr)
        left=[]
        right=[]
        for i in arr:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
        return randomized_quick_sort(left)+[pivot]+randomized_quick_sort(right)

# 三路快速排序                                                                                
def three_way_quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        left=[]
        middle=[]
        right=[]
        for i in arr:
            if i<pivot:
                left.append(i)
            elif i==pivot:
                middle.append(i)
            else:
                right.append(i)
        return three_way_quick_sort(left)+middle+three_way_quick_sort(right)