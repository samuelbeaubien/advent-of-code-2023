from typing import List


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

def squish_all_columns(rows: List[str]) -> List[str]:
    # Transpose
    table_transposed = ["".join(column) for column in zip(*rows)]
    table_squished_transposed = [squish_one_row(row) for row in table_transposed]
    table_squished = ["".join(column) for column in zip(*table_squished_transposed)]
    return table_squished

def calculate_load(rows: List[str]) -> int:
    loads = []
    for row, factor in zip(rows, range(len(rows), 0, -1)):
        loads.append(row.count('O')*factor)
    return sum(loads)

### SCRIPT ###  

file = open("src/day-14/input.txt", "r")
lines = file.readlines()
lines = [line.replace('/n', '') for line in lines]
lines = squish_all_columns(lines)
total_load = calculate_load(lines)

print("hello")
