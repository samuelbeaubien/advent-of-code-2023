file1 = open('src/day-1/input.txt')
lines = file1.readlines()
total = 0
for line in lines:
    digits = [int(c) for c in line if c.isdigit()]
    number = digits[0]*10 + digits[-1]
    total = total + number 

print (total)