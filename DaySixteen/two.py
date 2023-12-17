from collections import defaultdict


# class for everything to do with the beams
class Beams:
    def __init__(self, tiles):
        self.tiles = tiles
        self.energized = defaultdict(list)

    # function for adding all visited coordinates to the set
    def visited(self, x, y, direction) -> None:
        self.energized[(x, y)].append(direction)

    # function for giving the next coordinate
    def mv(self, x: int, y: int, direction: str) -> [int, int]:
        if direction == 'S':
            return x, y + 1
        elif direction == 'N':
            return x, y - 1
        elif direction == 'E':
            return x + 1, y
        elif direction == 'W':
            return x - 1, y
        else:
            print("Invalid direction")
            return None

    # model for handling interactions with contraptions
    def contraptions(self, x: int, y: int, direction: str) -> str:
        compass = ['S', 'E', 'N', 'W']

        if self.tiles[y][x] == '.':
            return direction
        elif self.tiles[y][x] == '/':
            # if we come from the top or bottom we move one direction anti-clockwise else clockwise
            if direction == 'S' or direction == 'N':
                return compass[compass.index(direction) - 1]
            else:
                return compass[(compass.index(direction) + 1) % 4]

        elif self.tiles[y][x] == '\\':
            # if we come from the top or bottom we move one direction clockwise else anti-clockwise
            if direction == 'S' or direction == 'N':
                return compass[compass.index(direction) + 1]
            else:
                return compass[compass.index(direction) - 1]

        elif self.tiles[y][x] == '|':
            if direction == 'S' or direction == 'N':
                return direction
            else:
                # new beam is created
                self.travel(x, y, 'N')

                # old beam continues in the other direction
                return 'S'

        elif self.tiles[y][x] == '-':
            if direction == 'E' or direction == 'W':
                return direction
            else:
                # new beam is created
                self.travel(x, y, 'W')

                # old beam continues in the other direction
                return 'E'

    # model for handling a beam
    def travel(self, x: int, y: int, direction: str) -> None:
        len_row = len(self.tiles[0])
        len_col = len(self.tiles)

        while True:

            # if the beam exits the grid or if the beam is in an infinite loop
            if x < 0 or x >= len(self.tiles) or y < 0 or y >= len_col or direction in self.energized[(x, y)]:
                return None

            # adding the tile to the set of energized tiles
            self.visited(x, y, direction)

            direction = self.contraptions(x, y, direction)

            # finding next tile
            x, y = self.mv(x, y, direction)

    # function for printing the grid
    def print_grid(self) -> None:
        print("\n")
        for y, line in enumerate(self.tiles):
            row = ""
            for x in range(len(line)):
                if (x, y) in self.energized:
                    row += '#'
                else:
                    row += line[x]
            print(row)

    def start_travel(self, x: int, y: int, direction: str) -> int:
        self.travel(x, y, direction)
        lava_tiles = len(self.energized)

        # clearing the energized tiles
        beams.energized = defaultdict(list)
        return lava_tiles


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# clearing input
lines = [line.strip('\n') for line in lines]
lines = [list(line) for line in lines]

# starting the simulation
beams = Beams(lines)

# visiting all the tiles on the edges of the grid
ans = 0
for y in range(len(lines)):
    al_y = beams.start_travel(0, y, 'E')
    ar_y = beams.start_travel(len(beams.tiles[0]) - 1, y, 'W')

    # updating the answer
    ans = max(ans, al_y, ar_y)

for x in range(len(lines[0])):
    al_x = beams.start_travel(x, 0, 'S')
    ar_x = beams.start_travel(x, len(beams.tiles) - 1, 'N')

    # updating the answer
    ans = max(ans, al_x, ar_x)


print("The maximum number of tiles that can be visited is", ans)
