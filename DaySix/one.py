import math
import re

# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting the time in a list; first remove the text and then replace all whitespaces with a single whitespace
times = (re.sub(r'(\s)+', ' ', re.sub(r'(\w)+:(\s)+', '', lines[0])).rstrip().split(' '))

# getting the distance in a list; same as the times removing words, then whitespaces and splitting
distances = (re.sub(r'(\s)+', ' ', re.sub(r'(\w)+:(\s)+', '', lines[1])).rstrip().split(' '))


# going over every item
ans = 1
for i, time in enumerate(times, 0):
    distance = int(distances[i])

    # the different parts of the equation
    a = int(time) / 2
    b = math.sqrt((int(time) / 2) ** 2 - distance)

    # getting the beginning and end; we want to take the whole integer under/over the number therefore we check if
    # the number is whole, so we subtract one to get the closes
    end = a + b
    if end == math.floor(end):
        end -= 1
    else:
        end = math.floor(end)

    begin = a - b
    if begin == math.ceil(begin):
        begin += 1
    else:
        begin = math.ceil(begin)

    ans *= end - begin + 1

print("The answer is: ", ans)
