def task():
    n = int(input())
    s = input()
    unique = [s[0]]
    current_task = s[0]
    for i in range(1, n):
        if s[i] == current_task:
            continue
        if s[i] in unique:
            print("NO")
            return
        else:
            unique.append(s[i])
            current_task = s[i]
    print("YES")

for i in range(int(input())):
    task()
        