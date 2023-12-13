from typing import List

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

class Node:
    def __init__(self, map_nodes, coordinates: List[int], symbol: str):
        self.map_nodes = map_nodes
        self.coord_i = coordinates[0]
        self.coord_j = coordinates[1]
        self.symbol = symbol
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def set_neighbors(self):
        """Set the north, east, west, south neighbors of the node.
        """
        if self.coord_i == 0:
            self.north = None
        else:
            self.north = self.map_nodes[self.coord_i - 1][self.coord_j]
        if self.coord_i == len(self.map_nodes) - 1:
            self.south = None
        else:
            self.south = self.map_nodes[self.coord_i + 1][self.coord_j]
        if self.coord_j == 0:
            self.west = None
        else:
            self.west = self.map_nodes[self.coord_i][self.coord_j - 1]
        if self.coord_j == len(self.map_nodes[0]) - 1:
            self.east = None
        else:
            self.east = self.map_nodes[self.coord_i][self.coord_j + 1]

    def get_connections(self):
        if self.symbol == '|':
            return [self.north, self.south]
        elif self.symbol == '-':
            return [self.east, self.west]
        elif self.symbol == 'L':
            return [self.north, self.east]
        elif self.symbol == 'J':
            return [self.north, self.west]
        elif self.symbol == '7':
            return [self.south, self.west]
        elif self.symbol == 'F':
            return [self.south, self.east]
        elif self.symbol == '.':
            return []
        elif self.symbol == 'S':
            return []
        
    def get_neighbors(self):
        neighbors = [
            self.north,
            self.south,
            self.east,
            self.west
        ]
        return [neighbor for neighbor in neighbors if neighbor is not None]

    # def __eq__(self, other):
    #     return (
    #         self.symbol == other.symbol and
    #         self.coord_i == other.coord_i and
    #         self.coord_j == other.coord_j
    #     )

def print_map_nodes(map_nodes):
    for line in map_nodes:
        print([node.symbol for node in line])

def find_s_node(map_nodes):
    for line in map_nodes:
        for node in line:
            if node.symbol == 'S':
                return node
            
def find_s_connections(node_s):
    neighbors = node_s.get_neighbors()
    connections = []
    for neighbor in neighbors:
        if node_s in neighbor.get_connections():
            connections.append(neighbor)
    return connections

class Analyser:
    def __init__(self, s_node):
        self.s_node = s_node
        self.max_distance = None

    def get_next_node(self, prev, node):
        connections = node.get_connections()
        if prev in connections:
            connections.remove(prev)
        return connections[0]
    
    def find_total_loop_length(self):
        s_connections = find_s_connections(self.s_node)
        # Select one of the connections randomly
        num_steps = 1
        prev_node = self.s_node
        cur_node = s_connections[0]
        while cur_node != self.s_node:
            connections = cur_node.get_connections()
            connections.remove(prev_node)
            next_node = connections[0]
            # Do the switch
            prev_node = cur_node
            cur_node = next_node
            num_steps += 1
        return num_steps
    
    def find_max_distance(self):
        total_loop_length = self.find_total_loop_length()
        max_distance = total_loop_length // 2
        return max_distance






### SCRIPT ###
# file = open("src/day-10/advanced_example.txt", "r")
# file = open("src/day-10/simple_example.txt", "r")
file = open("src/day-10/input.txt", "r")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
map_symbols = [list(line) for line in lines]
map_nodes = []
for i in range(len(map_symbols)):
    line_nodes = []
    for j in range(len(map_symbols[i])):
        line_nodes.append(Node(map_nodes, [i, j], map_symbols[i][j]))
    map_nodes.append(line_nodes)
for line in map_nodes:
    for node in line:
        node.set_neighbors()
# print_map_nodes(map_nodes)
s_node = find_s_node(map_nodes)
analyser = Analyser(s_node)
max_distance = analyser.find_max_distance()


print("hello")