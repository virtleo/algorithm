def merge_sort(arr):#分解过程
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    del arr
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

def merge(left,right):#合并过程
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

arr=[3,2,1,5,4]
print(merge_sort(arr))  

