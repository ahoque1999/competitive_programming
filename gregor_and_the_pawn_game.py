for i in range(int(input())):
    n = int(input())
    enemy = list(input())
    greg = list(input())

    count = 0
    for i in range(n):
        if greg[i] == "1" and i == 0:
            if enemy[i] == "0":
                count += 1 
            elif enemy[i + 1] == "1":
                enemy[i + 1] = "-1"
                count += 1
        elif greg[i] == "1" and i == n - 1:
            if enemy[i] == "0":
                count += 1            
            elif enemy[i - 1] == "1":
                enemy[i - 1] = "-1"
                count += 1        
        elif greg[i] == "1":
            if enemy[i] == "0":
                count += 1            
            elif enemy[i - 1] == "1":
                enemy[i - 1] = "-1"
                count += 1
            elif enemy[i + 1] == "1":
                enemy[i + 1] = "-1"
                count += 1
    print(count)