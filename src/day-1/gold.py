numbers =[
    ['one', '1'],
    ['two','2'],
    ['three','3'],
    ['four','4'],
    ['five','5'],
    ['six','6'],
    ['seven','7'],
    ['eight','8'],
    ['nine', '9']
    ]

file1 = open('src/day-1/test.txt')
file1 = open('src/day-1/input.txt')
lines = file1.readlines()
total = 0
for line in lines:
    first_num = None
    first_index = 1000
    last_num = None
    last_index = -1000
    new_line = line
    for num_str, num in numbers:
        try:
            cur_forward_index = line.index(num_str)
            if (cur_forward_index < first_index):
                first_index = cur_forward_index
                first_num = num
        except:
            pass
        try:
            cur_backward_index = line.rindex(num_str)
            if (cur_backward_index > last_index):
                last_index = cur_backward_index
                last_num = num
        except:
            pass
    chars = list(new_line)
    if (first_num != None):
        chars.insert(first_index, first_num)
    if (last_num != None):
        chars.insert(last_index+1, last_num)
    new_line = "".join(chars)
    digits = [int(c) for c in new_line if c.isdigit()]
    number = digits[0]*10 + digits[-1]
    print(f"{line} -> {new_line} -> {digits} -> {number}\n")
    total = total + number

print (total)
