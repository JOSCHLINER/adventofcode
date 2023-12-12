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
        self.grid_row_len = len(grid[0])
        self.grid_col_len = len(grid)

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
        self.grid[sy][sx] = '▓'

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

        # floodfill algorithm, that goes to the next tile until they meet[x, y, 0]

    # floodfill algorithm, that goes to the next tile until the two tubes meet; input for both tubes is [x, y]
    def flood(self, pl: list[int, int], pr: list[int, int]) -> bool:
        pl_x, pl_y, plc = pl[0], pl[1], 0
        pr_x, pr_y, prc = pr[0], pr[1], 0

        try:
            while True:

                # if the tubes connect
                if pl_x == pr_x and pl_y == pr_y:
                    # filling in the last tile
                    self.grid[pl_y][pl_x] = '▓'

                    # printing out the grid
                    print("The Final Grid is: ")
                    self.print_grid()
                    return True

                nl_x, nl_y = self.find_next(pl_x, pl_y)
                self.grid[pl_y][pl_x] = '▓'

                nr_x, nr_y = self.find_next(pr_x, pr_y)
                self.grid[pr_y][pr_x] = '▓'

                pl_x, pl_y, plc = nl_x, nl_y, plc + 1
                pr_x, pr_y, prc = nr_x, nr_y, prc + 1

        except Exception as error:
            print("An error occurred: ", error)
            return False

    # function for finding the next tile that should be moved to
    def find_next(self, cord_x: int, cord_y: int) -> (int, int):
        # getting the current pipe
        curr_pipe = self.grid[cord_y][cord_x]

        # print(self.grid[cord_y][cord_x])

        # getting the next directions of next pipe
        direction = self.pipes[curr_pipe]

        # determining the direction we are going
        mv_x, mv_y = self.move(cord_x, cord_y, direction[0])
        if self.grid[mv_y][mv_x] == '▓':
            mv_x, mv_y = self.move(cord_x, cord_y, direction[1])

        return mv_x, mv_y

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

    # algorithm for filling in all tiles that are accessible from outside with a dot
    def is_enclosed(self, x: int, y: int):
        if self.grid[y][x] == '░':
            return True
        elif self.grid[y][x] == 'I':
            return False

        def reach_edge(ex: int, ey: int) -> bool:
            if ex <= 0 or ex >= self.grid_row_len or ey <= 0 or ey >= self.grid_col_len:
                return True

            # if already visited or
            if (ex, ey) in visited or self.grid[ey][ex] == '▓':
                return False

            visited.add((ex, ey))

            # checking the other directions
            if reach_edge(ex + 1, ey) or \
                    reach_edge(ex - 1, ey) or \
                    reach_edge(ex, ey + 1) or \
                    reach_edge(ex, ey - 1):
                return True

            return False

        known = {'▓', '░', 'I'}
        def fill(fx: int, fy: int, reachable: bool) -> None:
            if fx < 0 or fx >= self.grid_row_len or fy < 0 or fy >= self.grid_col_len:
                return None

            if self.grid[fy][fx] in known:
                return None

            self.grid[fy][fx] = 'I' if reachable else '░'

            # going to adjacent tiles
            fill(fx + 1, fy, reachable)
            fill(fx - 1, fy, reachable)
            fill(fx, fy + 1, reachable)
            fill(fx, fy - 1, reachable)

        # checking if the tile is reachable from the outside
        visited = set()
        result = not reach_edge(x, y)

        print("The tile is reachable: ", result, " at: ", x, y)

        # filling in the maze
        fill(x, y, result)

        self.print_grid()

        return result


# creating the FloodFill class
labyrinth = FloodFill(lines)
length_rows = len(labyrinth.grid[0]) - 1

# if the flood fill successes
ans = 0
visited = {'▓', '░'}
if labyrinth.start_mv():

    # going over each row in the maze
    for r_i, row in enumerate(labyrinth.grid, 0):

        # left and right pointer find the two furthest items that were visited
        l, r = 0, len(row) - 1
        while l <= r and row[l] != '▓':
            l += 1

        while r >= l and row[r] != '▓':
            r -= 1

        # going over the items in between the pointers if they found something
        if l < r:

            for t in range(0, len(row) - 1): #range(l, r + 1):

                if row[t] not in visited:
                    if labyrinth.is_enclosed(t, r_i):
                        ans += 1

print("The number of tiles inbetween the maze which were not visited is: ", ans)
