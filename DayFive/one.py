import re


# class for handling the translation of ranges alongside their finding
class Translate:
    def __init__(self, items):
        self.items = items

        self.sort(items)

    # function for sorting the list of lists by its source range
    def sort(self, items):
        self.items = sorted(self.items, key=lambda x: x[1])
        print(self.items)

    # function for finding the index of the closes item to a given number
    def find(self, num: int):
        l, r = 0, len(self.items) - 1

        while l <= r:
            m = l + (r - l) // 2
            if self.items[m][1] > num:
                r = m - 1
            else:
                l = m + 1

        # returning the range item which is closes to said range
        return self.items[l - 1]

    # function for finding out to what value a number corresponds to
    def ranges(self, item, num: int) -> int:
        destination_range, source_range, range_len = item

        if source_range <= num < source_range + range_len:
            offset = num - source_range

            return offset + destination_range
        else:
            return num


'''
a = Translate([[50, 98, 2], [52, 50, 48]])

item = 55

b = a.find(item)
print(b)
print(a.ranges(b, item))
'''


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    lines.append('\n')


# function for getting all the data from the file
def extract_data(line: int):
    # getting the name
    name = re.sub(r'\s(\w)+:', '', lines[line]).rstrip()
    line += 1

    # splitting the data values and putting into a list as integers
    data = []
    while lines[line] != '\n':
        values_str = lines[line].rstrip().split(' ')
        values = list(map(int, values_str))

        data.append(values)
        line += 1

    return name, data, line


# getting all seeds
seeds = re.sub(r'(\w)+:\s', '', lines[0]).rstrip().split(' ')

# getting all the different translation values; here the order has to be correct
names, line = [], 0
while line < len(lines):
    trans_name, data, line = extract_data(line)
    if not data:
        line += 1
        continue

    # creating a new object with that data
    globals()[trans_name] = Translate(data)
    names.append(trans_name)

    line += 1

# function for calculating the location a seed has to be planted in
def get_location(num: int):
    value = num
    for name in names:
        index = globals()[name].find(value)
        value = globals()[name].ranges(index, value)
        # print("The value after: ", name, " is: ", value)

    return value

#a = Translate([[50, 98, 2], [52, 50, 48]])
#print(a.ranges([50, 98, 2], 52 ))


# go over each seed
min_location = float('inf')
for seed in seeds:

    location = get_location(int(seed))
    print(location)
    if location < min_location:
        min_location = location

print("The first plant to be planted is: ", min_location)
