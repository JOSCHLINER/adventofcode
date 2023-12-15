import re
from collections import defaultdict


# custom hashing algorithm HASHMAP
def HASHMAP(char: str, value: int) -> int:
    value += ord(c)
    value *= 17
    value %= 256

    return value


def get_item(item: str, rep: str or None, container: list) -> None:

    # checking if item is in list
    found_item = [x for x in container if item in x]

    # if item in list replace
    if rep is None:

        # if there is an item like it in the list
        if found_item:
            # replace the item
            container.pop(container.index(found_item[0]))
    else:
        if found_item:

            # remove the item
            container[container.index(found_item[0])] = rep
        else:
            container.append(rep)


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting the sequences
sequences = [line.rstrip().split(',') for line in lines]

# storage for boxes
boxes = defaultdict(list)

# going over each sequence
ans = 0
for sequence in sequences[0]:

    # getting label
    label = re.findall(r'\w+', sequence)[0]

    # getting the operation
    operation = re.findall(r'\W+', sequence)[0]

    # going over all characters in the letter and calculating the HASHMAP
    box = 0
    for c in label:
        box = HASHMAP(c, box)
    # print("The value for the label,", sequence, ", is: ", box)

    # if the operation is -
    if operation == '-':
        get_item(label, None, boxes[box])
    else:
        get_item(label, sequence.replace('=', ' '), boxes[box])

print("The boxes are: ", boxes)


# calculating the answer
for box in boxes:
    for slot, item in enumerate(boxes[box]):
        ans += (box + 1) * (slot + 1) * int(re.findall(r'\d+', item)[0])

print("The answer is: ", ans)
