for i in range(int(input())):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    print(min([s[i + 1] - s[i] for i in range(n -1)]))