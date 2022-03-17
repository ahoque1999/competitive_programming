import math
from timeit import repeat

for iteration in range(int(input())):
    n = int(input())
    squares = math.floor((n + 0.5) ** (1/2))
    cubes = math.floor((n + 0.5) ** (1/3))
    repeats = math.floor((n + 0.5) ** (1/6))
    print(squares + cubes - repeats)

