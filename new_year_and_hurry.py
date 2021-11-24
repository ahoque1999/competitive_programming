import math
from math import sqrt
n,k = list(map(int, input().split()))
root = (-5 + sqrt(5 ** 2 - 4 * 5 * (-480 + 2 * k)))/(2 * 5)
print(math.floor(root)) if n > root else print(n)