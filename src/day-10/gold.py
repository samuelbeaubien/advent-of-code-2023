from typing import List
from shapely import Polygon, MultiPoint
import numpy as np
import matplotlib.pyplot as plt

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

    def get_coordinates(self):
        return [self.coord_i, self.coord_j]
    
    def get_xy_coordinates(self):
        x = self.coord_j
        return [self.coord_j, self.coord_i]

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

    def get_cycle_coordinates(self):
        """Get the coordinates of the cycle.
        """
        cycle_coordinates = []
        # Add first coordinates
        cur_node = self.s_node
        cycle_coordinates.append(cur_node.get_coordinates())
        # Add the rest
        prev_node = cur_node
        cur_node = find_s_connections(cur_node)[0]
        while cur_node != self.s_node:
            cycle_coordinates.append(cur_node.get_coordinates())
            # Get next node
            connections = cur_node.get_connections()
            connections.remove(prev_node)
            next_node = connections[0]
            # Update
            prev_node = cur_node
            cur_node = next_node
        return cycle_coordinates
    
    def find_inside_area(self):
        self.cycle_coordinates = self.get_cycle_coordinates()
        self.shape = Polygon(self.cycle_coordinates)
        self.area = self.shape.area
        return int(self.area)
        




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
area = analyser.find_inside_area()

p = analyser.shape
xmin, ymin, xmax, ymax = p.bounds
x = np.arange(np.floor(xmin), np.ceil(xmax) + 1)  # array([0., 1., 2.])
y = np.arange(np.floor(ymin), np.ceil(ymax) + 1)  # array([0., 1., 2.])
points = MultiPoint(np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))]))
interior_coords = points.intersection(p)
interior_coords = [(p.x, p.y) for p in interior_coords.geoms]

num_dots = 0
for i, j in interior_coords:
    i = int(i)
    j = int(j)
    if [i,j] not in analyser.cycle_coordinates:
        num_dots += 1

# x,y = analyser.shape.exterior.xy
# plt.plot(x,y)
# plt.gca().invert_yaxis()
# plt.show()

print("hello")