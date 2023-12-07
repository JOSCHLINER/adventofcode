from collections import Counter, defaultdict


# class for handling all the ranking, counting and maximizing of a given hand
class Poker:
    def find_cards(self, card: str) -> int:
        cnt, joker = self.count(card)

        # looking if a joker is in the hand, if true, then we maximize that hand
        if joker > 0:
            hand_value = self.maximize(card, joker)
        else:
            hand_value = self.hand_value(cnt, card)

        # return the cards maximum value
        return hand_value

    # function for getting the value a given hand has
    def hand_value(self, cnt, card) -> int:

        if 5 in cnt:
            return 6
        elif 4 in cnt:
            return 5
        elif 3 in cnt:
            if 2 in cnt:
                return 4
            else:
                return 3
        elif cnt[2] == 2:
            return 2
        elif cnt[2] == 1:
            return 1
        else:
            return 0

    # function for maximizing a given hand
    def maximize(self, card: str, jokers: int) -> int:
        # removing the jokers from the card
        removed_joker = ""
        for c in card:
            if c == "J":
                continue
            removed_joker += c

        # getting amount of how often a type is found
        cnt, N_Jokers = self.count(removed_joker)

        # getting the biggest card
        max_cards = 0
        for item in cnt.keys():
            if item > max_cards:
                max_cards = item

        # removing the biggest card
        cnt[max_cards] -= 1
        if cnt[max_cards] <= 0:
            del cnt[max_cards]


        # adding item to cards
        cnt[max_cards + jokers] += 1
        #print(cnt, jokers)
        # getting the maximized hands value
        value = self.hand_value(cnt, card)

        return value

    # function for creating a dict of a given card
    def count(self, card: str):
        cnt = Counter(card)
        amount = defaultdict(int)
        for key in cnt.keys():
            amount[cnt[key]] += 1

        # getting the amount of jokers
        if 'J' in cnt:
            joker = cnt['J']
        else:
            joker = 0

        return amount, joker

    # function for sorting by letters; it isn't nice, but it works
    def rank(self, cards: list) -> list:
        SORT_ORDER = {"J": "1", "2": "a", "3": "b", "4": "c", "5": "d", "6": "e", "7": "f", "8": "g", "9": "h", "T": "i",
                       "Q": "k", "K": "l", "A": "m"}
        REVERSE_ORDER = {"a": "2", "b": "3", "c": "4", "d": "5", "e": "6", "f": "7", "g": "8", "h": "9", "i": "T",
                         "1": "J", "k": "Q", "l": "K", "m": "A"}

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

    value = poker_value.find_cards(hand)
    ranked[value].append(hand)

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
