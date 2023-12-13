
class Galaxy:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def get_shortest_distance(self, other, expanded_row_indices, expanded_columns_indices, expansion_factor):
        num_new_lines = expansion_factor - 1
        delta_i_unexpanded = abs(other.i - self.i)
        range_i = range(min(self.i, other.i), min(self.i, other.i) + delta_i_unexpanded)
        delta_i_expanded = delta_i_unexpanded
        for num in expanded_row_indices:
            if num in range_i:
                delta_i_expanded += num_new_lines
        delta_j_unexpanded = abs(other.j - self.j)
        range_j = range(min(self.j, other.j), min(self.j, other.j) + delta_j_unexpanded)
        delta_j_expanded = delta_j_unexpanded
        for num in expanded_columns_indices:
            if num in range_j:
                delta_j_expanded += num_new_lines
        return delta_i_expanded + delta_j_expanded



### SCRIPT ###

file = open("src/day-11/input.txt", "r")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [list(line) for line in lines]
unexpanded = list(lines)
expanded_row_indices = []
for i, line in enumerate(unexpanded):
    if all(char == '.' for char in line):
        expanded_row_indices.append(i)

# Expand the columns
columns = zip(*unexpanded)
expanded_columns_indices = []
for j, column in enumerate(columns):
    if all(char == '.' for char in column):
        expanded_columns_indices.append(j)

galaxies = []
galaxies_map = {}
for i, line in enumerate(unexpanded):
    for j, char in enumerate(line):
        if char == '#':
            galaxy = Galaxy(i, j)
            galaxies_map[f"{i}{j}"] = galaxy
            galaxies.append(galaxy)

# test_1_7 = galaxies_map["03"].get_shortest_distance(galaxies_map["17"], expanded_row_indices, expanded_columns_indices, 10)
# test_3_6 = galaxies[2].get_shortest_distance(galaxies[5])
# test_8_9 = galaxies[7].get_shortest_distance(galaxies[8])


sum = 0
for i, galaxy in enumerate(galaxies):
    other_galaxies = galaxies[i:]
    for other_galaxy in other_galaxies:
        sum += galaxy.get_shortest_distance(other_galaxy, expanded_row_indices, expanded_columns_indices, 1000000)


print("hello")





