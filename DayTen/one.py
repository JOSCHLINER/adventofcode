
# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# making the lines nice
for i, line in enumerate(lines):
    lines[i] = list(line.rstrip().replace('7', 'D'))


class FloodFill:
    def __init__(self, grid: list) -> None:
        self.grid = grid
        self.pipes = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['N', 'E'], 'J': ['N', 'W'], 'D': ['S', 'W'],
                      'F': ['S', 'E']}
        self.new_piping = {'|': '│', '-': '─', 'L': '└', 'J': '┘', 'D': '┐', 'F': '┌', 'S': '▒'}

    # function for finding the starting tile
    def find_start(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'S':
                    return x, y

    # function to find the tubes connected to the Start tile
    def start_mv(self):
        print(self.find_start())
        sx, sy = self.find_start()
        cords = []

        # replacing start with 0
        self.grid[sy][sx] = '▒'

        # finding the two tubes connected to the Start tile
        if self.grid[sy][sx + 1] in self.pipes:
            if 'W' in self.pipes[self.grid[sy][sx + 1]]:
                cords.append(sx + 1)
                cords.append(sy)

        if self.grid[sy][sx - 1] in self.pipes:
            if 'E' in self.pipes[self.grid[sy][sx - 1]]:
                cords.append(sx - 1)
                cords.append(sy)

        if self.grid[sy + 1][sx] in self.pipes:
            if 'N' in self.pipes[self.grid[sy + 1][sx]]:
                cords.append(sx)
                cords.append(sy + 1)

        if self.grid[sy - 1][sx] in self.pipes:
            if 'S' in self.pipes[self.grid[sy - 1][sx]]:
                cords.append(sx)
                cords.append(sy - 1)

        # calling the flood algorithm for filling in the maze
        return self.flood([cords[0], cords[1]], [cords[2], cords[3]])

    # floodfill algorithm, that goes to the next tile until the two tubes meet; input for both tubes is [x, y]
    def flood(self, pl: list[int, int], pr: list[int, int]) -> bool:
        pl_x, pl_y, plc = pl[0], pl[1], 0
        pr_x, pr_y, prc = pr[0], pr[1], 0

        while True:

            # if the tubes connect
            if pl_x == pr_x and pl_y == pr_y:
                # filling in the last tile
                self.grid[pl_y][pl_x] = '▒'

                # printing out the grid
                print("The Final Grid is: ")
                self.print_grid()
                return max(plc + 1, prc + 1)

            nl_x, nl_y, nl_p = self.find_next(pl_x, pl_y)
            self.grid[pl_y][pl_x] = nl_p  # str(pl[2] + 1)

            nr_x, nr_y, nr_p = self.find_next(pr_x, pr_y)
            self.grid[pr_y][pr_x] = nr_p  # str(pr[2] + 1)

            pl_x, pl_y, plc = nl_x, nl_y, plc + 1
            pr_x, pr_y, prc = nr_x, nr_y, prc + 1

    # function for finding the next tile that should be moved to
    def find_next(self, cord_x: int, cord_y: int) -> (int, int):
        # getting the current pipe
        curr_pipe = self.grid[cord_y][cord_x]

        # print(self.grid[cord_y][cord_x])

        # getting the next directions of next pipe
        direction = self.pipes[curr_pipe]
        sign = self.new_piping[curr_pipe]

        # determining the direction we are going
        mv_x, mv_y = self.move(cord_x, cord_y, direction[0])
        if self.grid[mv_y][mv_x] in self.new_piping.values():
            mv_x, mv_y = self.move(cord_x, cord_y, direction[1])

        return mv_x, mv_y, sign

    # function for moving to a specific tile
    def move(self, cord_x: int, cord_y: int, direction: str) -> (int, int):
        if direction == 'N':
            cord_y -= 1
        elif direction == 'S':
            cord_y += 1
        elif direction == 'E':
            cord_x += 1
        elif direction == 'W':
            cord_x -= 1

        return cord_x, cord_y

    # function for printing the whole grid out
    def print_grid(self):
        for row in self.grid:
            print(''.join(row))


# creating the FloodFill class
labyrinth = FloodFill(lines)

ans = labyrinth.start_mv()

print("The point furthest from you is: ", ans)
