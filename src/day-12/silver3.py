# DID NOT WORK

from enum import Enum

# class Symbol(Enum):
#     OPERATIONAL = "."
#     DAMAGED = "#"
#     UNKNOWN = "?"

# class Node:

#     def __init__(self, state_str, ):
#         self.state = Symbol(state_str)



# class Tree:



### SCRIPT ###

file = open("src/day-12/example.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [line.split(' ') for line in lines]
fields = [line[0] for line in lines]
groups = [[int(val) for val in list(line[1].split(','))] for line in lines]