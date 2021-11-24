for i in range(int(input())):
    candies = list(map(int, input().split()))
    print(sum(candies) // 2)