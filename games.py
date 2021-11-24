n = int(input())
h = []
a = []
for i in range(n):
    hi,ai = input().split()
    h.append(hi)
    a.append(ai)
count = 0
for i in range(n):
    count += a.count(h[i])
print(count)
