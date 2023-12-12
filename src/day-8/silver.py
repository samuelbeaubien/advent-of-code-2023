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


def find_it(network, instructions):
    steps = 0
    cur = network.nodes['AAA']
    old_instructions = instructions
    while True:
        instructions = old_instructions
        for instruction in instructions:
            if instruction == 'L':
                cur = cur.left
            elif instruction == 'R':
                cur = cur.right
            steps += 1
            if cur.name == 'ZZZ':
                return steps

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


result = find_it(network, instructions)


print("hello")
