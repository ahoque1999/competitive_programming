import math

for i in range(int(input())):
    n = int(input())
    target_sum = 2 ** n - 1
    target_start = (2 ** n - 1) // (2 ** (n//2) - 1)
    target_start = math.log(target_start, 2)
    upper = math.ceil(target_start)
    lower = math.floor(target_start) 
    closer = upper if 2 ** upper - 2 ** target_start <  2 ** target_start - 2 ** lower else lower
    print(abs(2 * (target_sum - 2 ** closer * (2 ** (n // 2) - 1)))) 