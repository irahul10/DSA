def Binary_Search(arr, x, si, ei):
    if si == len(arr):
        return -1

    mid = (si + ei) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return Binary_Search(arr,x,mid+1, ei) 
    else:
        return Binary_Search(arr, x, si, mid-1)


arr = [int(x) for x in input().split()]
x = int(input())
ans = Binary_Search(arr, x, 0, len(arr) - 1)
print(ans)