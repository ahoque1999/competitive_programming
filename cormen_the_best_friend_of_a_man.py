n, k = list(map(int, input().split()))
a = list(map(int,input().split()))

total = 0
for i in range(1, n):
    if a[i] < k - a[i - 1]:
        total += k - a[i - 1] - a[i] 
        a[i] = k - a[i -1]

print(total)
for ai in a:
    print(ai, end=" ")
print()