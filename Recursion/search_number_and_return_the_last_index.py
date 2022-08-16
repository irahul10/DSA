def search_and_return_last_index_of_number(arr, s, si):
    if si == len(arr):
        return -1
    
    ans = search_and_return_last_index_of_number(arr, s, si+1)
    if arr[si] == s:
        if ans != -1:
            return ans
        else:
            ans = si
    return ans
    

arr = [int(x) for x in input().split()]
search_number = int(input())
ans = search_and_return_last_index_of_number(arr, search_number, 0)
print(ans)