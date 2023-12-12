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

def find_it(network, instructions, starting_nodes):
    steps = 0
    cur_nodes = starting_nodes
    old_instructions = instructions
    while True:
        instructions = old_instructions
        for instruction in instructions:
            for node, node_index in zip(cur_nodes, range(len(cur_nodes))):
                if instruction == 'L':
                    cur_nodes[node_index] = node.left
                elif instruction == 'R':
                    cur_nodes[node_index] = node.right
            steps += 1
            is_true = True
            # Check if all the nodes in cur_nodes are at a node that ends by Z
            for node in cur_nodes:
                if node.name[2] != 'Z':
                    is_true = False
            if is_true:
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

starting_nodes = []
for node in network.nodes.values():
    if node.name[2] == 'A':
        starting_nodes.append(node)

result = find_it(network, instructions, starting_nodes)

print(result)
file2 = open("src/day-8/output.py", 'w')
file2.write(f"result = {result}")
file2.close()

print("hello")
