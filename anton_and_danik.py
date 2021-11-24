n = input()
s = input()
num_A = sum([1 for char in s if char is 'A'])
if num_A > (int(n) / 2):
    print("Anton")
elif num_A < (int(n) /2):
    print("Danik")
else:
    print("Friendship")