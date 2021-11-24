index_b = {
    0 : 2,
    1 : 0,
    2 : 1
}

for i in range(int(input())):
    xyz = list(map(int, input().split()))

    if len(set(xyz)) == 1:
        print("YES")
        print(f"{xyz[0]} {xyz[0]} {xyz[0]}")
    elif sorted(xyz)[1] == sorted(xyz)[2]:
        print("YES")
        a = min(xyz)
        result = [a, a, a]
        result[index_b[xyz.index(a)]] = max(xyz)
        print(f"{result[0]} {result[1]} {result[2]}")
    else:
        print("NO")