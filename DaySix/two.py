import math
import re

# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting the time in a list; first remove the text and then replace all whitespaces with a single whitespace
times = (re.sub(r'(\s)+', '', re.sub(r'(\w)+:(\s)+', '', lines[0])).rstrip())

# getting the distance in a list; same as the times removing words, then whitespaces and splitting
distances = (re.sub(r'(\s)+', '', re.sub(r'(\w)+:(\s)+', '', lines[1])).rstrip())

print(times, distances)


# going over every item
ans = 1

# the different parts of the equation
a = int(times) / 2
b = math.sqrt((int(times) / 2) ** 2 - int(distances))

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

ans *= abs(end - begin + 1)

print("The answer is: ", ans)
