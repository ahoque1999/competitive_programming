n,k = input().split()
n = int(n)
k = int(k)

for i in range(k):
    if n % 10 is 0:
        n = int(n/10) 
    else:
        n = n -1

print(n)
