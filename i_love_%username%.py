n = int(input())
scores = list(map(int, input().split()))

highest = scores[0]
lowest = scores[0]

counts = 0
for i in range(1,n):
    if scores[i] > highest:
        counts += 1
        highest = scores[i]
    elif scores[i] < lowest:
        counts += 1
        lowest = scores[i]
print(counts)