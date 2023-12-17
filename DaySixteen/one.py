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


# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# clearing input
lines = [line.strip('\n') for line in lines]
lines = [list(line) for line in lines]

# starting the simulation
beams = Beams(lines)
beams.travel(0, 0, 'E')

# printing the answer
beams.print_grid()
print("The total number of energized tiles is: ", len(beams.energized))
