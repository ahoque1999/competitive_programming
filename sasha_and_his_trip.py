n, v = list(map(int, input().split()))
distance = n - 1
if distance <= v:
    print(distance)
else:
    extra = distance - v
    extra_cost = sum([i for i in range(2, 2 + extra)])
    print(v + extra_cost)