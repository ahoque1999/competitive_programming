for iteration in range(int(input())):
    n = int(input())
    a, b, c = list(map(int, input().split()))
    # number of rock, paper and scissors for alice
    ra, pa, sa = a, b, c

    s = input()
    
    # number of rock, paper and scissors for bob
    rb = sum([1 for char in s if char == "R"])
    pb = sum([1 for char in s if char == "P"])
    sb = sum([1 for char in s if char == "S"])

    min_score = (n + 1) // 2

    if (min([ra, sb]) + min([pa, rb]) + min([sa, pb])) < min_score:
        print("NO")
        continue

    print("YES")
    
    rextra = ra - min([ra, sb])
    pextra = pa - min([pa, rb])
    sextra = sa - min([sa, pb])

    extra_pile = []

    for iteration in range(rextra):
        extra_pile.append("R")
    for iteration in range(pextra):
        extra_pile.append("P")
    for iteration in range(sextra):
        extra_pile.append("S")

    extra_pile_index = 0

    ra_count = ra
    pa_count = pa
    sa_count = sa

    for letter in s:
        if letter == "R":
            if pa_count > 0:
                print("P", end="")
                pa_count -= 1
            else:
                print(extra_pile[extra_pile_index], end="")
                extra_pile_index += 1
        elif letter == "P":
            if sa_count > 0:
                print("S", end="")
                sa_count -= 1
            else:
                print(extra_pile[extra_pile_index], end="")
                extra_pile_index += 1
        elif letter == "S":
            if ra_count > 0:
                print("R", end="")
                ra_count -= 1
            else:
                print(extra_pile[extra_pile_index], end="")
                extra_pile_index += 1
    print()