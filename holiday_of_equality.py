n = int(input())
a = list(map(int, input().split()))
print(sum([max(a) - ai for ai in a]))
