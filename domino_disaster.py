tile = {
    "U": "D",
    "D": "U",
    "L": "L",
    "R": "R",
}

for iteration in range(int(input())):
    n = int(input())
    s = input()
    print("".join([tile[char] for char in s])) 