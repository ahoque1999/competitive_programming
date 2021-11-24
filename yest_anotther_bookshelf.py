for i in range(int(input())):
    n = int(input())
    s = "".join(input().split()).strip("0")
    print(sum([1 for char in s if char == "0"]))