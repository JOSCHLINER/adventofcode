import re


# class for a tree graph
class GraphNode:
    def __init__(self, range_start: int, range_end: int):
        self.range_start = range_start
        self.range_end = range_end

        self.children = []

    def add_child(self, child_start: int, child_end: int) -> None:
        new_node = GraphNode(child_start, child_end)
        self.children.append(new_node)

        return new_node

    # function for getting all children of a node
    def get_children(self):
        return self.children

    # function for getting the start and end value of a node
    def value(self):
        return self.range_start, self.range_end

    def print_tree(self, depth=0):
        # Print the range of the current node
        print("  " * depth + f"Range: ({self.range_start}, {self.range_end})")

        # Recursively print the children
        for child in self.children:
            child.print_tree(depth + 1)


# function for finding the range a node should be in; AKA the bug function
def find_item(start: int, end: int, values):
    print("values:", values)
    l, r = 0, len(values) - 1

    while l <= r:
        m = l + (r - l) // 2
        if values[m][1] > start:
            r = m - 1
        else:
            l = m + 1

    # returning the range item which is closes to said range
    if l - 1 >= 0:
        print(start, end)
        print("The closes range is: ", values[l - 1])

        dest, src, ran_len = values[l - 1]
        ran_len -= 1
        src_start = src
        src_end = src + ran_len

        r_end = end

        # if start is in range, else its just its value
        if start <= src_end:
            start = (start - src_start) + dest

            # if end goes out of the range
            if end > src_end:
                end = dest + ran_len
                r_end = src_start + ran_len + 1
            else:
                r_end = end
                end = (end - src_start) + dest

        return start, end, r_end

    # if the range isn't defined
    else:

        # if the end overlaps with the next range
        if end >= values[0][1]:
            print("here")
            end = values[0][1] - 1
        return start, end, end


# function for getting the nodes ranges and adding them
def cnode(node: GraphNode, start: int, end: int, values: list):
    if start <= end:
        rnd_start, rnd_end, r_end = find_item(start, end, values)
        print(rnd_start, rnd_end, "\n Real end: ", r_end)
        node.add_child(rnd_start, rnd_end)

        cnode(node, r_end + 1, end, values)
    else:
        return None


def dfs(node: GraphNode, depth: int, values: list):
    print(node.value())
    children = node.get_children()

    # if we are the last node
    if not children:
        start, end = node.value()
        cnode(node, start, end, values[depth])

        return None

    for child in children:
        dfs(child, depth + 1, values)

#root = GraphNode(0, 44)
#dfs(root, 0, [[[39, 0, 15]], [[0, 15, 37]], [[37, 52, 2]]])

#'''
# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    lines.append('\n')


# getting all seeds and making them integers
seeds = re.sub(r'(\w)+:\s', '', lines[0]).rstrip().split(' ')
for i, seed in enumerate(seeds, 0):
    seeds[i] = int(seed)

# function for getting all the data from the file
def extract_data(line: int):
    line += 1

    # splitting the data values and putting into a list as integers
    data = []
    while lines[line] != '\n':
        values_str = lines[line].rstrip().split(' ')
        values = list(map(int, values_str))
        data.append(values)
        line += 1
    sorted_data = sorted(data, key=lambda x: x[1])
    return sorted_data, line

# getting all the range values from the file
values, line = [], 0
while line < len(lines):
    data, line = extract_data(line)
    if not data:
        line += 1
        continue

    values.append(data)
    line += 1

# function for getting the smallest and largest input values
seed_len = len(seeds)
seed_max, seed_min = float('-inf'), float('inf')
for i in range(0, seed_len, 2):
    values_start = seeds[i]
    value = values_start + seeds[i + 1]
    if value > seed_max:
        seed_max = value
    elif values_start < seed_min:
        seed_min = values_start

# creating the root node
root = GraphNode(seed_min, seed_max)

print(values)
# creating graph
for i, item in enumerate(values, 0):
    dfs(root, i, values)
root.print_tree()
#'''
'''
    def print_tree(self, depth=0):
        # Print the range of the current node
        print("  " * depth + f"Range: ({self.range_start}, {self.range_end})")

        # Recursively print the children
        for child in self.children:
            child.print_tree(depth + 1)
'''

'''        # if the item is in an undefined area after the last item
        else:

            # if it is not the last value
            if l - 2 < len(values):

                # if the end overlaps with the next range
                if end > values[l - 2][1]:
                    end = values[l - 2][0] - 1'''