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

cards_num_matches = []
for line in lines3:
    winning_str = line[0]
    gotten_str = line[1]
    winning_numbers = re.findall(r'\d+', winning_str)
    gotten_numbers = re.findall(r'\d+', gotten_str)
    matching = get_matching_numbers(winning_numbers, gotten_numbers)
    cards_num_matches.append(len(matching))

num_cards = len(cards_num_matches)
cards_number_instances = []
for card in cards_num_matches:
    cards_number_instances.append(1)

for i in range(num_cards):
    cur_card_num_matches = cards_num_matches[i]
    cur_card_num_instances = cards_number_instances[i]
    # The cur score tells the cards to add to (the cur_card_score next cards)
    # We add cur_card_num_instances to each of the next cards
    for j in range(1, cur_card_num_matches+1):
        cur_index = i + j
        if cur_index < num_cards:
            cards_number_instances[cur_index] += cur_card_num_instances




    # for cur_add in range(i):
    #     cur_index = i + cur_add
    #     if cur_index < len(cards_score):
    #         # How many to add?
    #         # Add 1*the number of cards
    #         cards_to_add = cards_number_instances[cur_index]
    #         cards_number_instances[cur_index] += cards_to_add

total_num_cards = 0
for score, number in zip(cards_num_matches, cards_number_instances):
    total_num_cards += number




print ("hello")

