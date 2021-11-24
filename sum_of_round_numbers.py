def task():    
    n = input()
    count = 0
    for d in n:
        if d != '0':
            count += 1
    print(count)
    for i in range(len(n)):
        if n[i] != '0':
            print(n[i] + '0' * (len(n) - i - 1), end=' ') 

t = int(input())
for i in range(t):
    task()
