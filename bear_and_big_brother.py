import math
a,b = input().split()
a = int(a)
b = int(b)
number = math.log( b / a ) / math.log( 3 / 2 )
if number.is_integer():
    print(int(number) + 1)
else:
    print(math.ceil(number))
