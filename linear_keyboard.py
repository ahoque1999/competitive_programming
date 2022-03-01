for iteration in range(int(input())):
    keyboard = input()
    word = input()
    n = len(word)

    dictionary = {keyboard[i]:i for i in range(26)}

    sum = 0
    for i in range(1, n):
        sum += abs(dictionary[word[i]] - dictionary[word[i - 1]])

    print(sum)