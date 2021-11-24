n = int(input())
a = list(map(int, input().split()))

length = [1] * n

for index in range(1, n):
    if a[index] <= 2 * a[index - 1]:
        length[index] = length[index - 1] + 1

print(max(length))