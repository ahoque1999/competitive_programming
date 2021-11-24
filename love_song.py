convert_letter_to_number = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
}

n, q = list(map(int, input().split()))
s = input()
summation = [0] * (n + 1)
for i in range(n):
    summation[i + 1] = summation[i] + convert_letter_to_number[s[i]]

for i in range(q):
    l, r = list(map(int, input().split()))
    l = l - 1
    print(summation[r] - summation[l])    