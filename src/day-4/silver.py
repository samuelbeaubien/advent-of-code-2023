import re

def get_matching_numbers(winning_numbers, gotten_numbers):
    """Return the numbers that match in both lists.
    """
    #Put winning in set
    winning_set = set()
    for number in winning_numbers:
        winning_set.add(number)
    matches = []
    for number in gotten_numbers:
        if number in winning_set:
            matches.append(number)
    return matches

def calculate_points(matches):
    """Calculate the points for the matches.
    """
    total = 0
    if len(matches) >0:
        total = 1
        matches.pop()
        for _ in matches:
            total *= 2
        return total
    else:
        return 0

### Script ###

file = open('src/day-4/input.txt', 'r')
lines_orig = file.readlines()
lines0 = [line[:-1] for line in lines_orig]
# Remove the first 9 characters from each line
lines1 = lines0
lines1 = [line.split(':') for line in lines1]
lines2 = [line[1] for line in lines1]
lines3 = [line.split('|') for line in lines2]

total_points = 0
for line in lines3:
    winning_str = line[0]
    gotten_str = line[1]
    winning_numbers = re.findall(r'\d+', winning_str)
    gotten_numbers = re.findall(r'\d+', gotten_str)
    matching = get_matching_numbers(winning_numbers, gotten_numbers)
    points= calculate_points(matching)
    print(points)
    total_points += points



print ("hello")

