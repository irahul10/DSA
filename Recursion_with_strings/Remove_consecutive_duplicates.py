def remove_consecutive_duplicates(s):
    if len(s) == 1:
        return s

    small_output = remove_consecutive_duplicates(s[1::])
    if small_output[0] == s[0]:
        return small_output
    else:
        small_output = s[0] + small_output
        return small_output


s = input()
ans = remove_consecutive_duplicates(s)
print(ans)