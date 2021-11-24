for i in range(int(input())):
    l, r = list(map(int, input().split()))
    print(f"{l} {2 * l}") if r // l > 1 else print(f"{-1} {-1}")