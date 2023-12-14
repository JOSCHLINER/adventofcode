def horizontal_detection(shadows: list[str]):
    def all_same(l: int, u: int):
        return all(shadows[l + i] == shadows[u - i] for i in range(1, u - l + 1))

    # from left
    row_left = shadows[0]
    for j in range(1, len(shadows)):
        if row_left == shadows[j]:
            if all_same(0, j):
                return 100 * (j + 1) // 2

    # from right
    row_right = shadows[-1]
    for j in range(len(shadows) - 2, -1, -1):
        if row_right == shadows[j]:
            if all_same(j, len(shadows) - 1):
                return 100 * (j + (len(shadows) - j) // 2)

    return -1


def vertical_detection(shadows: list[str]):
    def all_same(l: int, r: int) -> bool:
        return all(all(row[l + c] == row[r - c] for c in range(0, r - l + 1)) for row in shadows)

    # from left
    c_left = shadows[0][0]
    for j in range(1, len(shadows[0])):
        if c_left == shadows[0][j]:
            if all_same(0, j):
                return j // 2 + 1

    # from right
    c_right = shadows[0][-1]
    for j in range(len(shadows[0]) - 2, 0, -1):
        if c_right == shadows[0][j]:
            if all_same(j, len(shadows[0]) - 1):
                return j + (len(shadows[0]) - j - 1) // 2

    return -1


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    lines.append('\n')

# going over each pattern
ans, i = 0, 0
while i < len(lines):
    pattern = []
    while lines[i] != '\n':
        pattern.append(lines[i].rstrip())
        i += 1

    print("\n")
    # analyzing the pattern
    row_mirror = horizontal_detection(pattern)
    if row_mirror != -1:
        ans += row_mirror
        print(row_mirror)

        # printing the mirror line
        pattern.insert(row_mirror//100, '─'*len(pattern[0]))
        for row in pattern:
            print(row)

    else:
        a = vertical_detection(pattern)
        ans += a
        print(a)

        # printing the mirror line
        for row in pattern:
            modified_row = list(row)
            modified_row.insert(a, '│')
            print(''.join(modified_row))

    i += 1

print("The answer is: ", ans)
