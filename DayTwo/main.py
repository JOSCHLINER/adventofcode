import re

FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    print(lines)

ans = 0
biggest_allowed = {'red': 12, 'green': 13, 'blue': 14}
for game, line in enumerate(lines, 1):
    found = {'red': 0, 'blue': 0, 'green': 0}

    games_str = re.sub(r'(.)+:.', '', line).rstrip()
    games = games_str.split(';')

    # going over each round of drawn cubes
    for i, item in enumerate(games, 0):
        # splitting the round result in the different cubes
        games[i] = item.split(',')

        # getting result of every cube that has been drawn in a single round
        for individual in games[i]:

            # getting the amount and type of cube
            times = int(re.search(r'(\d)+', individual).group())
            item = re.search(r'(\w+)$', individual).group()

            # checking if we have new info about the amount
            if found[item] < times:
                found[item] = times

    # adding all the items together
    row = 1
    for key in found.keys():
        row *= found[key]
    ans += row

print("The answer is: ", ans)
