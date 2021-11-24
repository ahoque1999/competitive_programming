n, a, b, c = list(map(int, input().split()))

totals = []
if a != b and b != c and a != c:
    max_a_iteration = n // a + 1
    max_b_iteration = n // b + 1
    for index_a in range(max_a_iteration):
        for index_b in range(max_b_iteration):
            for_c = n - index_a * a - index_b * b
            if for_c % c == 0 and for_c >= 0:
                totals.append(index_a + index_b + for_c // c)

uniques = list(set([a, b, c]))
if len(uniques) == 2:
    first = uniques[0]
    second = uniques[1]
    max_first_iteration = n // first + 1
    for index_first in range(max_first_iteration):
        for_second = n - index_first * first
        if for_second % second == 0 and for_second >= 0:
            totals.append(index_first + for_second// second) 

if 1 in uniques:
    print(n)
elif len(uniques) == 1:
    print(n // a)
else:
    print(max(totals))