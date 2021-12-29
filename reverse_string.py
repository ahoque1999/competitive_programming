def return_possible_candidates(t):
    candidates = []
    n = len(t)
    for i in range(n):
        check = min([i - 0, n - 1 - i])
        left = t[i - check: i]
        right = t[i + 1: i + 1 + check][::-1]
        if left == right:
            if n - 1 - i > i - 0:
                candidate = t[i:n][::-1]
            else:
                candidate = t[0:i + 1]
            candidates.append(candidate)
    return candidates

for iteration in range(int(input())):
    s = input()
    t = input()

    found = False
    candidates = return_possible_candidates(t)
    for candidate in candidates:
        if candidate in s:
            found = True
            break
    print("YES") if found else print("NO")