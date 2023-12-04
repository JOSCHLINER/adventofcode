'''
Intuition:
    To solve this problem we first have to extract all winning and scratched numbers. Then we iterate over the scratched
    numbers and look if they can be found in the winning numbers.

Algorithm:
    1) split numbers
    2) add the winning numbers to a dict
    3) going over the scratched numbers and looking if they can be found under the winning numbers
        3.1) adding the maximum to the points between 1 and *2, this adds 1 the first round and else multiplies with two
'''

import re

FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


# going over every line
ans = 0
for game, line in enumerate(lines, 0):

    # removing starting string and splitting the numbers
    game_str = re.sub(r'(.)+:\s', '', line).rstrip()
    winning, scratched = game_str.split('|')

    # extracting the winning / scratched numbers
    winning = winning.split(' ')
    scratched = scratched.split(' ')

    # adding the winning numbers to a dict
    winning_numbers = {}
    for num in winning:
        if num == '':
            continue
        winning_numbers[num] = 0

    # going over every scratched number and looking if it is a winning number
    win = 0
    for num in scratched:
        if num == '':
            continue

        # if it is we either add 1, for the first win, or multiply it by two
        if num in winning_numbers:
            win = max(1, win * 2)

    ans += win

print("The answer is: ", int(ans))