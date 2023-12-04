'''
Intuition:
    The problem consists of first of all finding a number. Then we can check if there lays any symbol adjacent to it.

Algorithm:
    1) Go over every line
    2) Go over every x value
        2.1) If we find a digit we add it to a string
        2.2) Once the number ends we won't find a digit but the string will not be empty.
        2.4) We go over all items from before the start of the number to the end of the symbol for the line
        before, the same line and the line after
        2.3.2) If the item is a symbol we add it to our answer
'''

FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    print(lines)

# define the length; x is -2 as we have \n at the end (definitely wasn't an annoying bug to find)
y_length = len(lines)
x_length = len(lines[0]) - 2


# function for checking is a given item is a symbol
def is_symbol(x: int, y: int) -> bool:
    if x >= x_length or y >= y_length or x < 0 or y < 0:
        return False

    symbol = lines[y][x]
    if symbol == '.' or symbol.isnumeric():
        return False

    print("True")
    return True


# function for testing all values around a given number
def maneuver_around(x: int, y: int, num_len: int) -> bool:
    y += 1

    # checking the line above before as well as the same line
    for i in range(3):

        # iterating over every symbol from one before to one after
        for j in range(x - num_len - 1, x + 1):
            if is_symbol(j, y - i):
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

            # call maneuver function to test if a symbol is adjustment to the number
            if maneuver_around(x, y, len(num)):
                ans += int(num)
            num = ""
        x += 1

print("The Answer is: ", ans)
