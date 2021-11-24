def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = i * result
    return result

def ncr(n, r):
    return factorial(n) // factorial(r) // factorial(n -r)

n = int(input())

print(ncr(2 * n - 2, n - 1))