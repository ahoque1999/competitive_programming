def convert_win(character):
    return 1 if character == "?" else int(character)

def convert_loss(character):
    return 0 if character == "?" else int(character)

for iteration in range(int(input())):
    turns = []
    predictions = input()
    t1 = [predictions[index] for index in range(10) if index % 2 == 0]
    t2 = [predictions[index] for index in range(10) if index % 2 == 1]

    # if t1 wins
    t1_t1_wins = [convert_win(prediction) for prediction in t1]
    t2_t1_wins = [convert_loss(prediction) for prediction in t2]
    t1_cumulative_score = [0] * 5
    for index in range(5):
        t1_cumulative_score[index] = t1_cumulative_score[index - 1] + t1_t1_wins[index]
    t2_cumulative_score_t1_wins = [0] * 5
    for index in range(5):
        t2_cumulative_score_t1_wins[index] = t2_cumulative_score_t1_wins[index - 1] + t2_t1_wins[index]    
    t2_max_possible = [0] * 5
    for index in range(5):
        t2_max_possible[index] = t2_cumulative_score_t1_wins[index] + 4 - index
    
    for turn in range(1, 10):
        if t2_max_possible[(turn - 1) // 2] < t1_cumulative_score[(turn) // 2]:
            turns.append(turn + 1)
            break

    # if t2 wins
    t1_t2_wins = [convert_loss(prediction) for prediction in t1]
    t2_t2_wins = [convert_win(prediction) for prediction in t2]
    t2_cumulative_score_t2_wins = [0] * 5
    for index in range(5):
        t2_cumulative_score_t2_wins[index] = t2_cumulative_score_t2_wins[index - 1] + t2_t2_wins[index]
    t1_cumulative_score_t2_wins = [0] * 5
    for index in range(5):
        t1_cumulative_score_t2_wins[index] = t1_cumulative_score_t2_wins[index - 1] + t1_t2_wins[index]
    t1_max_possible = [0] * 5
    for index in range(5):
        t1_max_possible[index] = t1_cumulative_score_t2_wins[index] + 4 - index
    
    for turn in range(1, 10):
        t1_score = t1_max_possible[turn // 2]
        t2_score = t2_cumulative_score_t2_wins[(turn - 1) // 2]
        if t1_score < t2_score:
            turns.append(turn + 1)
            break
    
    print(min(turns)) if turns else print(10)