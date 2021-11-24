for i in range(int(input())):
    h, m = list(map(int, input().split()))
    minutes = 60 - m if m != 0 else 0
    minutes += (24 - h - 1) * 60 if m != 0 else (24 -h) * 60
    print(minutes)