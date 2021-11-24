n = int(input())
a = list(map(int, input().split()))

seen_4 = 0
seen_8 = 0
seen_15 = 0
seen_16 = 0
seen_23 = 0
seen_42 = 0

extra = 0

for index in range(n):
    if a[index] == 4:
        seen_4 += 1
    
    elif a[index] == 8:
        if seen_8 + 1 <= seen_4:
            seen_8 += 1
        else:
            extra += 1
    
    elif a[index] == 15:
        if seen_15 + 1 <= seen_8:
            seen_15 += 1
        else:
            extra += 1
    elif a[index] == 16:
        if seen_16 + 1 <= seen_15:
            seen_16 += 1
        else:
            extra += 1
    
    elif a[index] == 23:
        if seen_23 + 1 <= seen_16:
            seen_23 += 1
        else:
            extra += 1
    
    elif a[index] == 42:
        if seen_42 + 1 <= seen_23:
            seen_42 += 1
        else:
            extra += 1

bins = [seen_4, seen_8, seen_15, seen_16, seen_23, seen_42]

minimum = min(bins)

extra += sum([value - minimum for value in bins])
print(extra)