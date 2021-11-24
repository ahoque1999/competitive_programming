d = sorted(list(map(int, input().split())))

short = d[0] + d[1]
if d[2] > short:
    print(2 * short)
else:
    print(sum(d))