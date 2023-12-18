
# opening the file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

ans = 0
# removing everything except the hex number
lines = [line.rstrip().split('(')[-1][1:-1] for line in lines]
print(lines)


# coordinates for all the corners
plane = [(0, 0)]

x, y = 0, 0
boundary_points = 0
for line in lines:
    a = 1

    steps = int(line[:5], 16)

    direction = int(line[-1])
    if direction == 0:
        nx, ny = 1, 0
    elif direction == 1:
        nx, ny = 0, 1
    elif direction == 2:
        nx, ny = -1, 0
    elif direction == 3:
        nx, ny = 0, -1
    else:
        print("Invalid input, please check your input. The input was: ", line)
        break

    x += nx * steps
    y += ny * steps
    plane.append((x, y))

    boundary_points += steps

# calculating the area inside the polygon using the formular for calculating the area of a simple polygon
# see https://en.wikipedia.org/wiki/Polygon
area = 0
point = plane[0]
for i in range(1, len(plane)):
    next_point = plane[i]
    area += point[0] * next_point[1] - next_point[0] * point[1]

    point = next_point

# using Picks formula to calculate the amount of points inside of the calculated area
area = abs(area) // 2
interior_points = area - boundary_points / 2 + 1

print(int(interior_points + boundary_points))
