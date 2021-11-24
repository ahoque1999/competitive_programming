guest = list(input())
residence = list(input())
combined = guest + residence
combined.sort()
letters = list(input())
letters.sort()
print("YES") if letters == combined else print("NO")

