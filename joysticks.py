MAX = 1500

first = [0] * MAX
second = [0] * MAX

a,b = list(map(int, input().split()))

first[0] = a
second[0] = b

for i in range(1, MAX):
    if first[i - 1] == 0 or second[i - 1] == 0:
        print(i - 1)
        break
    
    if first[i - 1] == 1 and second[i - 1] == 1:
        print(i - 1) 
        break

    if first[i - 1] <= second[i - 1]:
        first[i] = first[i - 1] + 1
        second[i] = second[i -1] - 2
    else:
        second[i] = second[i - 1] + 1
        first[i] = first[i - 1] - 2