def is_list_sorted(arr, si):
    if si == len(arr)-1:
        return True
    
    if arr[si] > arr[si+1]:
        return False
    
    ans = is_list_sorted(arr, si+1)
    return ans
    
arr = [int(x) for x in input().split()]
print(is_list_sorted(arr, 0))