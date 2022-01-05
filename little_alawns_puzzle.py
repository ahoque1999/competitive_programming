def find(n):
    while True:
        if n == parent[n]:
            return n
        else:
            n = parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        parent[a] = b

for iteration in range(int(input())):
    n = int(input())
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))

    parent = [i for i in range(n + 1)]
    for i in range(n):
        union(r1[i], r2[i])
    
    groups = 0
    for i in range(1, n + 1):
        if i == parent[i]:
            groups += 1
    
    result = 1
    for i in range(groups):
        result = (2 * result) % (10**9 + 7)
    print(result)