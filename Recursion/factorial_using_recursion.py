def Factorial_using_recursion(n):
    if n == 0:
        return 1

    ans = Factorial_using_recursion(n - 1)
    return n * ans

n = int(input())
print(Factorial_using_recursion(n))