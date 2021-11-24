def encode(char):
    return 1 if char == "x" else 0

n = int(input())
s = input()

encoded = [encode(char) for char in s]

for i in range(1, n):
    if s[i -1] == "x" and s[i] == "x":
        encoded[i] = encoded[i -1] + 1
        encoded[i - 1] = 0

concerned_lengths = [ele - 2 for ele in encoded if ele >= 3]

print(sum(concerned_lengths))