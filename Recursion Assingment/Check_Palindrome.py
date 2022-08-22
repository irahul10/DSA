def check_palindrome(str, i, j):
    if i >= j:
        return True
    
    if str[i] != str[j]:
        return False

    ans = check_palindrome(str, i+1, j-1)
    if ans:
        return True
    else:
        return False
    
str = input()
ans = check_palindrome(str, 0, len(str) - 1)
print(ans)
