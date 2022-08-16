def sum_of_array_elements(arr, si):
    if si == len(arr)-1:
        return arr[si]
    
    ans = sum_of_array_elements(arr, si+1)
    ans = ans + arr[si]
    return ans


arr = [int(x) for x in input().split()]
print(sum_of_array_elements(arr, 0))