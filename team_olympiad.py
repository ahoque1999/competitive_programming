n = int(input())
ti = list(map(int, input().split()))

ones = [i + 1 for i, t in enumerate(ti) if t == 1]
twos = [i + 1 for i, t in enumerate(ti) if t == 2]
threes = [i + 1 for i, t in enumerate(ti) if t == 3]

teams = min([len(ones), len(twos), len(threes)])
print(teams)
for i in range(teams):
    print(f'{ones[i]} {twos[i]} {threes[i]}')