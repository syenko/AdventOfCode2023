from functools import cmp_to_key

f = open("input.txt", "r")
# f = open("test.txt", "r")

lines = [x.strip() for x in f]

ans = 0

vals_to_num = "J23456789TQKA"

FIVE = 7
FOUR = 6
FULL = 5
THREE = 4
TWO = 3
ONE = 2
HIGH = 1

class Hand():
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

        self.card_count = {i: 0 for i in range(len(vals_to_num))}

        joker_count = 0
        for card in hand:
            if card == 'J':
                joker_count += 1
            else:
                self.card_count[vals_to_num.index(card)] += 1

        self.type = HIGH

        max_count = max(self.card_count.values()) + joker_count
        if max_count == 5:
            self.type = FIVE
        elif max_count == 4:
            self.type = FOUR
        elif max_count == 3:
            twos_count = list(self.card_count.values()).count(2)
            if (joker_count == 0 and twos_count == 1) or (joker_count == 1 and twos_count == 2):
                self.type = FULL
            else:
                self.type = THREE
        elif max_count == 2:
            twos_count = list(self.card_count.values()).count(2)
            if twos_count == 2:
                self.type = TWO
            else:
                self.type = ONE

    def __repr__(self):
        return "{} {} ({})".format(self.hand, self.bid, self.type)
def compare(a, b):
    if a.type < b.type:
        return -1
    elif a.type > b.type:
        return 1
    else:
        for i, char in enumerate(a.hand):
            val_a = vals_to_num.index(char)
            val_b = vals_to_num.index(b.hand[i])
            if val_a < val_b:
                return -1
            elif val_a > val_b:
                return 1

    return 0

hands = []

for line in lines:
    hand, bid = line.split()
    bid = int(bid)

    hands.append(Hand(hand, bid))

hands = sorted(hands, key=cmp_to_key(compare))

print(hands)

for i, hand in enumerate(hands):
    ans += (i + 1) * hand.bid

print(ans)

f.close()