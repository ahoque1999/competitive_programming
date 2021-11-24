factors = []
for i in range(4):
    factors.append(int(input()))
print(sum([1 for i in range(1, int(input()) + 1) if any(i % f == 0 for f in factors)]))