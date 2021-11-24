def get_num(start_char, end_char):
    numbers = list(map(int, [start_char, end_char]))
    return(min([max(numbers) - min(numbers), min(numbers) + 10 - max(numbers)]))

n = int(input())
start = input()
end = input()

print(sum([get_num(start[i], end[i]) for i in range(n)]))