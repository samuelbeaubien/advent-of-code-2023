def find_and_replace(lines, line_number, char_number):
    """Extend left and right to get the full number, then replace with '.'.
    """
    # Extend left
    start_index = char_number
    while start_index > 0:
        if lines[line_number][start_index-1].isnumeric():
            start_index -= 1
        else:
            break
    # Extend right
    end_index = char_number
    while end_index < len(lines[line_number])-1:
        if lines[line_number][end_index+1].isnumeric():
            end_index += 1
        else:
            break
    # Get the number
    number = int(''.join(lines[line_number][start_index:end_index+1]))
    # Replace
    for i in range(start_index, end_index+1):
        lines[line_number][i] = '.'
    return number

def check_around(lines, line_number, char_number):
    """Will only return a number if a gear is surrounded by two numbers
    """
    total_numbers = 0
    total = 1
    # Check above:
    if line_number > 0:
        if char_number > 0:
            if lines[line_number-1][char_number-1].isnumeric():
                total_numbers +=1
                total *= find_and_replace(lines, line_number-1, char_number-1)
        if lines[line_number-1][char_number].isnumeric():
            total_numbers +=1
            total *= find_and_replace(lines, line_number-1, char_number)
        if char_number < len(lines[line_number-1])-1:
            if lines[line_number-1][char_number+1].isnumeric():
                total_numbers +=1
                total *= find_and_replace(lines, line_number-1, char_number+1)
    # Check left and right:
    if char_number > 0:
        if lines[line_number][char_number-1].isnumeric():
            total_numbers +=1
            total *= find_and_replace(lines, line_number, char_number-1)
    if char_number < len(lines[line_number])-1:
        if lines[line_number][char_number+1].isnumeric():
            total_numbers +=1
            total *= find_and_replace(lines, line_number, char_number+1)
    # Check below:
    if line_number < len(lines)-1:
        if char_number > 0:
            if lines[line_number+1][char_number-1].isnumeric():
                total_numbers +=1
                total *= find_and_replace(lines, line_number+1, char_number-1)
        if lines[line_number+1][char_number].isnumeric():
            total_numbers +=1
            total *= find_and_replace(lines, line_number+1, char_number)
        if char_number < len(lines[line_number+1])-1:
            if lines[line_number+1][char_number+1].isnumeric():
                total_numbers +=1
                total *= find_and_replace(lines, line_number+1, char_number+1)
    if total_numbers == 2:
        return total
    else:
        return 0

### Script ###
file = open('src/day-3/input.txt', 'r')
lines_orig = file.readlines()
lines = [list(line[:-1]) for line in lines_orig]

total = 0
for line, line_number in zip(lines, range(len(lines))):
    for char, char_number in zip(line, range(len(line))):
        if (not char.isnumeric()) and (char != '.'):
            if (char == '*'):
                total += check_around(lines, line_number, char_number)
print(total)
            
    

print("hello")