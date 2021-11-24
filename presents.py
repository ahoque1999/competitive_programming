n = int(input())
p = list(map(int,input().split()))
for i in range(n):
    print(p.index(i + 1) + 1, end=" ")