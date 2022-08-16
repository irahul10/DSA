def print_n_natural_number(n):
    if n == 0:
        return
    print(n)
    print_n_natural_number(n-1)

n = int(input())
print_n_natural_number(n)