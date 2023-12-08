import re


# class for the nodes
class Node:
    def __init__(self, name, left, right):
        self.left = left
        self.right = right
        self.name = name


# class for moving through the graph
class Graph:
    def __init__(self):
        self.nodes = {}

    def left(self, node_name):
        left_node = self.nodes[node_name].left
        return self.nodes[left_node].name

    def right(self, node_name):
        right_node = self.nodes[node_name].right
        return self.nodes[right_node].name

    def add_node(self, node_name, left, right):
        self.nodes[node_name] = Node(node_name, left, right)


root = Graph()

# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting move pattern
move_pattern = lines[0].rstrip()
del lines[0]

def pattern(step: int):
    return move_pattern[step % len(move_pattern)]

# creating the Graph
for line in lines:
    if line == '\n':
        continue

    inputs = re.sub(r'(\W)+', ' ', line).rstrip().split(' ')
    print(inputs),

    # add the node to the graph
    root.add_node(inputs[0], inputs[1], inputs[2])

print(root.nodes)

# traversing the graph
curr, steps = 'AAA', 0
while curr != 'ZZZ':
    curr_step = pattern(steps)
    if curr_step == 'L':
        curr = root.left(curr)
    else:
        curr = root.right(curr)

    steps += 1

print("The steps to get to ZZZ with your pattern is: ", steps)