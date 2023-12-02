class Round:
    def __init__(self, data):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.process_input(data)

    def process_input(self, data):
        self.initial_data = data
        num_color_list = data.split(', ')
        for num_color in num_color_list:
            [num_str, color] = num_color.split(' ')
            if color == 'red':
                self.red = int(num_str)
            elif color == 'green':
                self.green = int(num_str)
            elif color == 'blue':
                self.blue = int(num_str)

class Game:
    def __init__(self, line):
        self.max_reds = 0
        self.max_greens = 0
        self.max_blues = 0
        self.process_input(line)

    def compare_colors(self, round):
        if round.red > self.max_reds:
            self.max_reds = round.red
        if round.green > self.max_greens:
            self.max_greens = round.green
        if round.blue > self.max_blues:
            self.max_blues = round.blue

    def process_input(self, line):
        self.initial_line = line
        line = line[0:-1]
        line = line.strip()
        [header, data] = line.split(': ')
        [_, num] = header.split(' ')
        self.number = int(num)

        rounds_str = data.split('; ')
        self.rounds = []
        for round_str in rounds_str:
            round = Round(round_str)
            self.rounds.append(round)
            self.compare_colors(round)

class Bag:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def is_game_possible(self, game):
        if self.red < game.max_reds:
            return False
        if self.green < game.max_greens:
            return False
        if self.blue < game.max_blues:
            return False
        return True


### SCRIPT ###
bag = Bag(12, 13, 14)
# file = open('src/day-2/test.txt')
file = open('src/day-2/input.txt')
lines = file.readlines()
games = []
# Create games
for line in lines:
    game = Game(line)
    games.append(game)
# Check if games are possible and add numbers    
total = 0
for game in games:
    if (bag.is_game_possible(game)):
        total += game.number
print(total)

