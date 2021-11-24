n = int(input())
num_of_rooms = 0
for i in range(n):
    p,q = map(int,input().split())
    if (q - p) >= 2:
        num_of_rooms += 1
print(num_of_rooms)    