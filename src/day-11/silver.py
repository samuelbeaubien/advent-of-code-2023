
class Galaxy:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def get_shortest_distance(self, other):
        delta_i = abs(other.i - self.i)
        delta_j = abs(other.j - self.j)
        return delta_i + delta_j



### SCRIPT ###

file = open("src/day-11/input.txt", "r")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [list(line) for line in lines]
unexpanded = list(lines)
expanded = []
for line in unexpanded:
    if all(char == '.' for char in line):
        expanded.append(list(line)) # Add twice
    expanded.append(list(line))

# Expand the columns
columns = zip(*expanded)
expanded_columns = []
for j, column in enumerate(columns):
    if all(char == '.' for char in column):
        expanded_columns.append(list(column))
    expanded_columns.append(list(column))

expanded = list(zip(*expanded_columns))
galaxies = []
galaxies_map = {}
for i, line in enumerate(expanded):
    for j, char in enumerate(line):
        if char == '#':
            galaxy = Galaxy(i, j)
            galaxies_map[f"{i}{j}"] = galaxy
            galaxies.append(galaxy)

sum = 0
for i, galaxy in enumerate(galaxies):
    other_galaxies = galaxies[i:]
    for other_galaxy in other_galaxies:
        sum += galaxy.get_shortest_distance(other_galaxy)

# test_1_7 = galaxies_map["04"].get_shortest_distance(galaxies_map["19"])
# test_3_6 = galaxies[2].get_shortest_distance(galaxies[5])
# test_8_9 = galaxies[7].get_shortest_distance(galaxies[8])

print("hello")





