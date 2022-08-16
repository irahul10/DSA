def merge(arr, arr1, arr2):
    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i+=1
            k+=1
        else:
            arr[k] = arr2[j]
            j+=1
            k+=1
    
    while i < len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1

    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1

def merge_sort(arr):
    if len(arr) == 1:
        return
    
    mid = len(arr) // 2

    arr1 = arr[0:mid]
    arr2 = arr[mid::]

    merge_sort(arr1)
    merge_sort(arr2)
    merge(arr, arr1, arr2)

arr = [int(x) for x in input().split()]
merge_sort(arr)
print(arr)