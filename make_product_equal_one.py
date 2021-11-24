n = int(input())
a = list(map(int, input().split()))

zero = False
first_pass = a
first_pass_cost = [0] * n
for i in range(n):
    to_one = abs(a[i] - 1)
    to_minus_one = abs(a[i] + 1)
    if to_one == 0 or to_minus_one == 0:
        continue 
    if a[i] == 0:
        zero = True
    first_pass[i] = 1 if to_one <= to_minus_one else -1
    first_pass_cost[i] = min([to_one, to_minus_one])

product = first_pass[0]
for i in range(1, n):
    product *= first_pass[i]
    
if product == 1:
    print(sum(first_pass_cost))
elif zero:
    print(sum(first_pass_cost))
else:
    print(sum(first_pass_cost) + 2)