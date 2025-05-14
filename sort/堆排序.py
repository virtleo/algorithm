def heap_sort(arr):
    n=len(arr)
    # Build max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    # Extract elements from heap one by one
    for i in range(n-1,0,-1):
        # Move current root to end
        arr[i],arr[0]=arr[0],arr[i]
        # call max heapify on the reduced heap
        heapify(arr,i,0)

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

# Testing the code
arr=[64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print(arr)