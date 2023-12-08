'''
I did not find the solution for how to get the amount of steps myself, though I implemented it myself.
'''


import re
from math import gcd


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

    # function for getting the left node name
    def left(self, node_name):
        left_node = self.nodes[node_name].left
        return self.nodes[left_node].name

    # function for getting the right node name
    def right(self, node_name):
        right_node = self.nodes[node_name].right
        return self.nodes[right_node].name

    # function for adding a node to the graph
    def add_node(self, node_name, left, right):
        self.nodes[node_name] = Node(node_name, left, right)


# creating the graph
root = Graph()

# opening file
FILE_PATH = "../input.txt"
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

# getting move pattern and removing it from the list to not cause errors later
move_pattern = lines[0].rstrip()
del lines[0]


# returning the pattern
def pattern(step: int):
    return move_pattern[step % len(move_pattern)]


# creating the Graph
a_nodes = []
for line in lines:
    if line == '\n':
        continue

    # getting the input
    inputs = re.sub(r'(\W)+', ' ', line).rstrip().split(' ')

    # if the node ends with 'A', we add it to our list of A nodes
    if inputs[0][-1] == 'A':
        a_nodes.append(inputs[0])

    # add the node to the graph
    root.add_node(inputs[0], inputs[1], inputs[2])

# going over all the A nodes
a_nodes_steps = []
for node in a_nodes:
    curr, steps = node, 0
    while curr[-1] != 'Z':
        curr_step = pattern(steps)
        if curr_step == 'L':
            curr = root.left(curr)
        else:
            curr = root.right(curr)

        steps += 1
    a_nodes_steps.append(steps)

# getting the LCM of all the steps (https://stackoverflow.com/a/42472824)
lcm = 1
for i in a_nodes_steps:
    lcm = lcm * i // gcd(lcm, i)

print("The amount of steps that need to be taken is: ", lcm)
