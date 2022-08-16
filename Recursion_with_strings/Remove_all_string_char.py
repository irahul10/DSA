def remove_string_char(s, removing_char):
    if len(s) == 0:
        return s
    
    small_output = remove_string_char(s[1::], removing_char)
    if s[0] == removing_char:
        return small_output
    else:
        small_output = s[0] + small_output
    return small_output


s = input()
removing_char = input()
ans = remove_string_char(s, removing_char)
print(ans)