def get_number_from_the_string():
    return sum([int(s) for s in input().split() if s.isdigit()])

n = int(input())
counter = 0
for attempt in range(n):
    if get_number_from_the_string() > 1:    
        counter += 1
print(counter)

