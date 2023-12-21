
# function for printing the tiles
def print_tiles(visited):
    print("\n The tiles that have been visited are: ")
    for row in range(col_len):
        out = ""
        for col in range(row_len):
            if (col, row) in visited:
                out += '@'
            else:
                out += lines[row][col]

        print(out)


# opening the file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
lines = [list(line.rstrip()) for line in lines]

row_len = len(lines[0])
col_len = len(lines)

# finding the start position
q = []
for y in range(col_len):
    for x in range(row_len):
        # if the tile is the start tile
        if lines[y][x] == 'S':

            # going to all directions
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                # adding the tile to the queue
                q.append((i, j))
            break

# set for storing all the visited tiles
tiles = set()

# going each step and counting the tiles that can be reached in that step
tiles_even, tiles_odd = 0, 0
for step in range(64):

    # going over each step we can take
    tiles_count, nq = 0, []
    while q:

        # getting the current position
        x, y = q.pop(0)

        # if the tile has been visited
        if (x, y) in tiles:
            continue

        # if the tile is out of bounds
        elif 0 > x or x >= row_len or 0 > y or y >= col_len:
            continue

        # if the tile is a wall
        elif lines[y][x] == '#':
            continue

        # saving the current position
        tiles.add((x, y))
        tiles_count += 1

        # going in the different directions
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            # adding the new position to the queue for the next step
            nq.append((nx, ny))

    # updating the step tile counter
    if step % 2 == 0:
        tiles_odd += tiles_count
    else:
        tiles_even += tiles_count

    # updating the steps queue to go to the next step
    q = nq

print_tiles(tiles)
print("Tiles that could be reached in 64 steps", tiles_even)
