[a,b] = input().split()
scores = input().split()
defining_score = int(scores[int(b) -1])
count = 0
for number in scores:
    if int(number) > 0 and int(number) >= defining_score:
        count += 1
print(count)
