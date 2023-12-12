# https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset

from math import gcd
from functools import reduce


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

class NodeAnalysis:
    def __init__(self, initial_node, instructions):
        self.initial_node = initial_node
        self.steps = 0
        self.cur_node = initial_node
        self.end_results = []
        self.cycle_instructions = instructions
        
    def analyze(self, num_cycles):
        for _ in range(num_cycles):
            instructions = self.cycle_instructions
            for char in instructions:
                if char == 'L':
                    self.cur_node = self.cur_node.left
                elif char == 'R':
                    self.cur_node = self.cur_node.right
                self.steps += 1
                if self.cur_node.name[2] == 'Z':
                    if self.end_results == []:
                        output = [self.steps, self.cur_node.name, self.steps]
                    else:
                        diff = self.steps - self.end_results[-1][0]
                        output = [self.steps, self.cur_node.name, diff]
                    self.end_results.append(output)

# def find_it(instructions, starting_nodes):
#     steps = 0
#     cur_nodes = starting_nodes
#     old_instructions = instructions
#     while True:
#         instructions = old_instructions
#         for instruction in instructions:
#             for node, node_index in zip(cur_nodes, range(len(cur_nodes))):
#                 if instruction == 'L':
#                     cur_nodes[node_index] = node.left
#                 elif instruction == 'R':
#                     cur_nodes[node_index] = node.right
#             steps += 1
#             is_true = True
#             # Check if all the nodes in cur_nodes are at a node that ends by Z
#             for node in cur_nodes:
#                 if node.name[2] != 'Z':
#                     is_true = False
#             if is_true:
#                 return steps
            

            

### SCRIPT ###
file = open("src/day-8/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
instructions = lines[0]
lines = lines[2:]
network = Network()
for line in lines:
    name = line.split(' = ')[0]
    node = Node(name)
    network.add_node(node)
for line in lines:
    name = line.split(' = ')[0]
    directions = line.split(' = ')[1]
    directions = directions.replace('(', '')
    directions = directions.replace(')', '')
    directions = directions.split(', ')
    left = directions[0]
    right = directions[1]
    cur = network.nodes[name]
    left = network.nodes[left]
    right = network.nodes[right]
    cur.left = left
    cur.right = right

starting_nodes = []
for node in network.nodes.values():
    if node.name[2] == 'A':
        starting_nodes.append(node)

analyses = []
for node in starting_nodes:
    analysis = NodeAnalysis(node, instructions)
    analysis.analyze(1000)
    analyses.append(analysis)

cycle_lengths = []
for analysis in analyses:
    cycle_lengths.append(analysis.end_results[-1][2])
cur_total = 1
for length in cycle_lengths:
    cur_total = abs(cur_total * length) // gcd(cur_total, length)

print("hello")


