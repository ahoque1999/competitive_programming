from collections import Counter

for iteration in range(int(input())):
    frequecy = Counter(input())

    doubles = []
    singles = []

    for key in frequecy:
        if frequecy[key] == 2:
            doubles.append(key)
        else:
            singles.append(key)
    
    print(''.join(doubles) * 2 + ''.join(singles))