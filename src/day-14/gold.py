from typing import List, Dict
import numpy as np

TABLE: Dict[str, int] = {}

def squish_one_row(row: str) -> str:
    parts = row.split('#')
    new_parts = []
    for part in parts:
        new_part = ""
        num_boulders = part.count('O')
        num_dots = len(part) - num_boulders
        new_part = 'O'*num_boulders + '.'*num_dots
        new_parts.append(new_part)
    squished_row = "#".join(new_parts)
    return squished_row

def squish_all_columns_toward_north(rows: List[str]) -> List[str]:
    # Transpose
    table_transposed = ["".join(column) for column in zip(*rows)]
    table_squished_transposed = [squish_one_row(row) for row in table_transposed]
    table_squished = ["".join(column) for column in zip(*table_squished_transposed)]
    return table_squished

def squish_array(array: np.array) -> np.array:
    rows = array.tolist()
    rows = ["".join(row) for row in rows]
    rows = squish_all_columns_toward_north(rows)
    rows = [list(row) for row in rows]
    array = np.array(rows)
    return array

def squish_rot(array: np.array) -> np.array:
    array = squish_array(array)
    array = np.rot90(array, k=-1)
    return array

def find_first_repeated_state(rows: List[str], step_number: int) -> List[str]:
    rows = [list(row) for row in rows]
    array = np.array(rows)
    while (True):
        array_str = array.tostring()
        if (array_str in TABLE):
            return array, step_number
        else:
            TABLE[array_str] = step_number
            array = squish_rot(array)
            step_number += 1

def calculate_load(rows: List[str]) -> int:
    loads = []
    for row, factor in zip(rows, range(len(rows), 0, -1)):
        loads.append(row.count('O')*factor)
    return sum(loads)

### SCRIPT ###  
file = open("src/day-14/input.txt", "r")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
num_quads = 1000000000
total_num_steps = 4 * num_quads
rows = lines
first_repeated_array, cur_step_number = find_first_repeated_state(rows, 0)
prev_step_number = TABLE.get(first_repeated_array.tostring())
num_steps_in_cycle = cur_step_number - prev_step_number
remaining_steps = total_num_steps - cur_step_number
remainder = remaining_steps % num_steps_in_cycle

arr = first_repeated_array
# Do remaining steps
for _ in range(remainder):
    arr = squish_rot(arr)

lines = ["".join(row) for row in  arr.tolist()]


total_load = calculate_load(lines)

print(total_load)
print("hello")
