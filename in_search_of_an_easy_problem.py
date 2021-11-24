n = int(input())
opinions = list(map(int, input().split()))
hard = False
for opinion in opinions:
    # print(opinion)
    if opinion == 1:
        hard = True
        break
if hard:
    print("HARD")
else:
    print("EASY")