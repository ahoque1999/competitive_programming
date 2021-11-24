convert= {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25,
}

for i in range(int(input())):
    letters = [0] * 26
    n = int(input())
    for i in range(n):
        s = input().strip()
        for char in s:
            letters[convert[char]] += 1
    check = True
    for letter in letters:
        if letter % n != 0:
            check = False
    print("YES") if check else print("NO")