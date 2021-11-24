a = list(map(int, input().split()))
s = input()
print(sum([a[int(si) - 1] for si in s]))