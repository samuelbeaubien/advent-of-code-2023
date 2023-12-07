import math

def get_num_ways(race_time, cur_dist_record):
    cur_dist_record = cur_dist_record + 0.1
    part_2 = math.sqrt(race_time**2 - 4*cur_dist_record)
    max = math.floor((race_time + part_2)/2)
    min = math.ceil((race_time - part_2)/2)
    r = range(min, max+1)
    return len(r)

file = open("src/day-6/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [[int(x) for x in line.split(':')[1].split(" ") if x.isdigit()] for line in lines]
times = lines[0]
lengths = lines[1]
time = "".join([str(time) for time in times])
time = int(time)
max_length = "".join([str(length) for length in lengths])
max_length = int(max_length)

answer = get_num_ways(time, max_length)





print("hello")
