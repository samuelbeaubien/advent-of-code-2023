import re

def get_regex_for_field(field):
    field = field.replace('.', r'\.')
    field = field.replace('#', '#')
    field = field.replace('?', '([.]|[#])')
    return field

def get_regex_for_group(group):
    regex = '[.]*'
    for number in group:
        regex += f'#{{{number}}}[.]+'
    #Remove the + and replace by star
    regex = regex[:-1] + '*'
    regex = '^' + regex
    regex = regex + '$'
    return regex
    
def intersection_regex(regex1, regex2):
    """Create a regex that is the intersection of two regexes
    """
    return f'(?=[{regex1}])(?=[{regex2}])'

def get_permutations(field: str):
    if not '?' in field:
        return [field]
    else:
        option_1 = str(field).replace('?', '.', 1)
        option_2 = str(field).replace('?', '#', 1)
        return get_permutations(option_1) + get_permutations(option_2)
    
def get_permutations_optimized(field: str):
    permutations = [field]
    while '?' in permutations[0]:
        option_1 = [permutation.replace('?', '.', 1) for permutation in permutations]
        option_2 = [permutation.replace('?', '#', 1) for permutation in permutations]
        permutations = option_1 + option_2
    return permutations

def get_num_possibilities(field: str, group_regex: str):
    all_permutations = get_permutations_optimized(field)
    num_possibilities = 0
    matched = []
    for permutation in all_permutations:
        if re.match(group_regex, permutation):
            num_possibilities += 1
            matched.append(permutation)
    return num_possibilities

### SCRIPT ###

file = open("src/day-12/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [line.split(' ') for line in lines]
fields = [line[0] for line in lines]
fields_regex = [get_regex_for_field(field) for field in fields]
groups = [list(line[1].split(',')) for line in lines]
groups_regex = [get_regex_for_group(group) for group in groups]
# combined_regex = [intersection_regex(field, group) for field, group in zip(fields_regex, groups_regex)]

possibilities = []
for field, group_regex in zip(fields, groups_regex):
    possibilities.append(get_num_possibilities(field, group_regex))

total = sum(possibilities)





print ("hello")

