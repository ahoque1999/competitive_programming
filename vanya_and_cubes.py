def sums(n):
    return sum([(1 + i) * i // 2 for i in range(1, n + 1)])

def get_number(n):
    i = 1
    while(True):
        if n < sums(i):
            return i - 1
        i += 1

n = int(input())
print(get_number(n))