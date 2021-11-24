n,t = input().split()
n = int(n)
t = int(t)
queue = input()

for i in range(t):
    queue = queue.replace("BG","GB")
print(queue)