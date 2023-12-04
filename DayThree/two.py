'''
Intuition:
    The problem consists of first of all finding a number. Then we can check if there lays any gears adjacent to it. If
    there are, we save the gear alongside all the number we find next to it. When done we can calculate the ratio of
    each gear.

Algorithm:
    It is the same as on star one but with the difference that when a gear is found we add it, and the number next to it
    to a dictionary with a list as index. Then we later go over every gear we found and check if it has more than one
    part number next to it. If it has we calculate the ratio and add it to the answer.
'''
from collections import defaultdict

FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    print(lines)

# define the length; x is -2 as we have \n at the end
y_length = len(lines)
x_length = len(lines[0]) - 2

gears = defaultdict(list)


# function for checking is a given item is a symbol
def is_gear(x: int, y: int, num: str) -> bool:
    if x >= x_length or y >= y_length or x < 0 or y < 0:
        return False

    # we check if it is a gear, if it is we add it to the gear alongside the number
    symbol = lines[y][x]
    if symbol == '*':
        gears[x, y].append(int(num))
        return True
    return False


# function for testing all values around a given number
def maneuver_around(x: int, y: int, num_len: int, num: str) -> bool:
    y += 1

    # checking the line above before as well as the same line
    for i in range(3):

        # iterating over every symbol from one before to one after
        for j in range(x - num_len - 1, x + 1):
            if is_gear(j, y - i, num):
                return True

    return False


ans = 0
for y, line in enumerate(lines, 0):

    # we move over every x value
    x, num = 0, ""
    while x < x_length:

        # going over a number if one is found
        while line[x].isnumeric():
            num += str(line[x])
            x += 1

        # if there is a number that has ended num won't be empty
        if num != "":

            # call maneuver function to test if a gear is adjustment to the number
            maneuver_around(x, y, len(num), num)

            num = ""
        x += 1


# going over each gear we found
for gear in gears.keys():

    # if the gear has more than 1 number next to it, we proceed
    if len(gears[gear]) > 1:

        # going over every item and calculating the ratio from it
        ratio = 1
        for item in gears[gear]:
            ratio *= item
        ans += ratio

print("The Answer is: ", ans)
