
# custom hashing algorithm
def hash(char: str, value: int) -> int:
    value += ord(c)
    value *= 17
    value %= 256

    return value


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting the sequences
sequences = [line.rstrip().split(',') for line in lines]

# going over each sequence
ans = 0
for sequence in sequences[0]:

    # going over all characters in a sequence and hashing it
    value = 0
    for c in sequence:
        value = hash(c, value)
    # print("The value for the word is: ", value)

    ans += value

print("The answer is: ", ans)
