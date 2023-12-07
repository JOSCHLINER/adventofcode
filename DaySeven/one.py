from collections import Counter, defaultdict


class Poker:

    # function for getting the value a given hand has
    def get_value(self, card: str) -> int:
        cnt = self.count(card)

        if 5 in cnt:
            value = 7
        elif 4 in cnt:
            value = 6
        elif 3 in cnt and 2 in cnt:
            value = 5
        elif 3 in cnt:
            value = 4
        elif cnt[2] == 2:
            value = 3
        elif cnt[2] == 1:
            value = 2
        else:
            value = 1

        return value

    # function for creating a dict of a given card
    def count(self, card: str) -> defaultdict:
        cnt = Counter(card)
        amount = defaultdict(int)
        for key in cnt.keys():
            amount[cnt[key]] += 1

        return amount

    # function for sorting by letters; it isn't nice, but it works
    def rank(self, cards: list) -> list:
        SORT_ORDER = {"2": "a", "3": "b", "4": "c", "5": "d", "6": "e", "7": "f", "8": "g", "9": "h", "T": "i", "J": "j", "Q": "k", "K": "l", "A": "m"}
        REVERSE_ORDER = {"a": "2", "b": "3", "c": "4", "d": "5", "e": "6", "f": "7", "g": "8", "h": "9", "i": "T", "j": "J", "k": "Q", "l": "K", "m": "A"}


        converted_strs = []
        for card in cards:
            converted = ""
            for c in card:
                converted += SORT_ORDER[c]
            converted_strs.append(converted)

        original_strs = []
        for card in sorted(converted_strs):
            original = ""
            for c in card:
                original += REVERSE_ORDER[c]
            original_strs.append(original)

        return original_strs


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


# putting each card in the right division and adding it to the values dict
poker_value = Poker()
cards_bet, ranked = {}, [[], [], [], [], [], [], []]
for line in lines:
    hand, bet = line.rstrip().split(' ')
    cards_bet[hand] = int(bet)

    value = poker_value.get_value(hand)
    ranked[value - 1].append(hand)

# sorting each division by letter values
for i, division in enumerate(ranked):
    cards_sorted = poker_value.rank(division)
    ranked[i] = cards_sorted

ans, rank = 0, 1
for division in ranked:
    for card in division:
        ans += cards_bet[card] * rank
        rank += 1


print("The answer is: ", ans)

