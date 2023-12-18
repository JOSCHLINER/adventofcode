
# opening the file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

ans = 0
lines = [line.rstrip().split(' ') for line in lines]


# building the outlines of the perimeter
plane = [[('#', None)]]
x, y = 0, 0
for instruction in lines:

    # getting what direction to move in
    direction = instruction[0]
    if direction == 'R':
        md_x, md_y = 1, 0
    elif direction == 'L':
        md_x, md_y = -1, 0
    elif direction == 'U':
        md_x, md_y = 0, -1
    elif direction == 'D':
        md_x, md_y = 0, 1

    # adding the nodes for each instruction
    color = instruction[2][1:-1]
    for i in range(int(instruction[1])):
        x, y = x + md_x, y + md_y

        # adding new tiles when necessary
        if x >= len(plane[0]):
            for row in plane:
                row.append(('.', None))

        elif x < 0:
            x += 1
            for row in plane:
                row.insert(0, ('.', None))
        elif y >= len(plane):
            plane.append([('.', None)] * len(plane[0]))
        elif y < 0:
            y += 1
            plane.insert(0, [('.', None)] * len(plane[0]))

        plane[y][x] = ('#', color)
        ans += 1

# getting a tile inside the perimeter, this is done by going all the way to the edge of the plane and looking for a tile
# if we then go one tile down and right we have a tile we can use, if it is not a tile we can go down until we hit one
# this works only assuming the perimeter is at least three blocks wide at any point
for x, col in enumerate(plane[0]):
    if col[0] == '#':
        sx = x + 1
        sy = 1

        break

# calculating the volume inside the perimeter
q = [(sx, sy, 0, 1)]
while q:
    ix, iy, dx, dy = q.pop(0)

    # if we have hit a wall or a tile we have already visited
    if plane[iy][ix][0] == '#':
        continue

    ans += 1
    plane[iy][ix] = ('#', plane[iy][ix][1])

    # going in all the other directions except the one we came from
    for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (nx, ny) != (-dx, -dy):
            q.append((ix + nx, iy + ny, nx, ny))

print("The volume of the lava is: ", ans)
