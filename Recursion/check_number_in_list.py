def search_number_in_list_using_recursion(arr, s, si):
    if si == len(arr):
        return False
    
    if arr[si] == s:
        return True
    
    ans = search_number_in_list_using_recursion(arr, s, si+1)
    if ans:
        return True
    else:
        return False
    

arr = [int(x) for x in input().split()]
search_number = int(input())
ans = search_number_in_list_using_recursion(arr, search_number, 0)
print(ans)


# Return Imdex of searching element.
def search_number_in_list_using_recursion_return_index(arr, s, si):
    if si == len(arr):
        return -1
    
    if arr[si] == s:
        return si
    
    ans = search_number_in_list_using_recursion_return_index(arr, s, si+1)
    if si == -1:
        return -1
    else:
        return ans
    

arr = [int(x) for x in input().split()]
search_number = int(input())
ans = search_number_in_list_using_recursion_return_index(arr, search_number, 0)
print(ans)