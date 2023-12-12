FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

'''
    isspelled()
        This function tests if at a given point the letters in a given line are a number spelled out.
    
    Intuition:
        We are given a string and have to find out if this string is a number. For this we have to test all possible length of a string to find if there is a spelled number in there.
    
    Algorithm:
        1) Test if the given word is long enough
        2) We iterate over every length a spelled letter can have
            2.1) Test the string from the back/front to this index
'''

LETTERS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
def isspelled(word: str, rev: bool) -> int:
    length = len(word)
    if length < 3:
        return 0

    if rev:
        for i in range(3, min(6, length + 1)):
            if word[-i:] in LETTERS:
                return LETTERS[word[-i:]]
    else:
        for i in range(3, min(6, length + 1)):

            if word[:i] in LETTERS:
                return LETTERS[word[:i]]

    return 0

'''
print("Front to back: ", isspelled('threetkccstz', False))
print("Reversed: ", isspelled('tkccstzthree', True))
54094
'''


ans = 0
for line in lines:

    l, r = 0, 0
    length_line = len(line)

    # left pointer
    for lp in range(length_line):
        letter = line[lp]
        if letter.isnumeric():
            l = int(letter)
            break
        else:
            value = isspelled(line[:lp+1], True)
            if value != 0:
                l = value
                break

    # right pointer
    for rp in range(length_line - 1, -1, -1):
        letter = line[rp]
        if letter.isnumeric():
            r = int(letter)
            break
        else:
            value = isspelled(line[rp-1:], False)
            if value != 0:
                r = value
                break

    print("Line: ", line, "l: ", l, "r: ", r)
    ans += (l * 10) + r

print("The total sum of all values is: ", ans)

