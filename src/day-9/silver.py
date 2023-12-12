
def get_next_value(numbers):
    lines = []
    lines.append(list(numbers))
    while not all(v == 0 for v in lines[-1]):
        cur_line = lines[-1]
        new_line = []
        for i in range(len(cur_line) - 1):
            new_line.append(cur_line[i + 1] - cur_line[i])
        lines.append(new_line)
    # DEBUG
    # for line in lines:
    #     print(f"{line}")
    cur_last_number = 0
    reversed = list(lines)
    reversed.reverse()
    for line in reversed:
        # print(f"{line}")
        cur_last_number = line[-1] + cur_last_number
        # print(f"{cur_last_number}")
    
    # if (lines[-1] == []):
    #     for line in lines:
    #         print(f"{line}")

    return cur_last_number

file = open("src/day-9/input.txt")
# file = open("src/day-9/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [list((int(num) for num in line.split(' '))) for line in lines]

total = 0
for line in lines:
    next_val = get_next_value(line)
    total += next_val
    print("#################### \n\n")
    
print(total)
print ("hello")