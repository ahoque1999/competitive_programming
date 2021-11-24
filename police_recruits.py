n = int(input())
events = list(map(int, input().split()))
reserve = 0
crime = 0
for event in events:
    if event == -1 and reserve == 0:
        crime += 1
    elif event == -1:
        reserve -= 1
    else:
        reserve += event
print(crime)