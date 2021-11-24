k,n,w = input().split()
k = int(k)
n = int(n)
w = int(w)
borrowed_amount = int((1 + w) * w / 2 * k - n)
if borrowed_amount > 0:
    print(borrowed_amount)
else: 
    print(0)
