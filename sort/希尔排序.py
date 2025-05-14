def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap=gap//2
    return arr

arr=[5,3,8,6,2,7,1,4]
print(shell_sort(arr))
def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            key=arr[i]
            j=i-gap
            while j>=0 and arr[j]>key:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap]=key
        gap=gap//2
    return arr
arr=[5,3,8,6,2,7,1,4]
print(shell_sort(arr))