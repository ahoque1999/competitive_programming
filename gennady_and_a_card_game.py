card_table = input()
rank = card_table[0]
suite = card_table[1]

cards_hand = input().split()
ranks = [card[0] for card in cards_hand]
suites = [card[1] for card in cards_hand]

def check_presence(list, card):
    for cards in list:
        if cards == card:
            return True
    return False

print("YES") if check_presence(ranks, rank) or check_presence(suites, suite) else print("NO")