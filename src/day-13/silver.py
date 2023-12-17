from typing import List

def is_full_reflection(pattern: List[str], reflection_row):
    # Split list at reflection_row
    first_half = pattern[:reflection_row]
    second_half = pattern[reflection_row:]
    # Equalize
    diff = abs(len(first_half) - len(second_half))
    if len(first_half) > len(second_half):
        first_half = first_half[diff:]
    if len(second_half) > len(first_half):
        second_half = second_half[:-diff]
    second_half_reversed = second_half
    second_half_reversed.reverse()
    return first_half == second_half_reversed


def get_reflection_row(pattern: List[str]) -> int|None:
    """The reflection row is the row directly after the reflection line.
    """
    # Find two rows that are the same
    for i in range(len(pattern)):
        j = i+1
        if j < len(pattern):
            cur = pattern[i]
            next = pattern[j]
            if cur == next:
                if is_full_reflection(pattern, j):
                    return j
    return None

def get_reflection_column(pattern: List[str]) -> int|None:
    pattern_ll = [list(s) for s in pattern]
    columns_as_rows = ["".join(row) for row in zip(*pattern_ll)]
    return get_reflection_row(columns_as_rows)


### SCRIPT ###

file = open("src/day-13/input.txt", "r")
input = file.read()
file.close()
patterns = input.split('\n\n')
patterns = [pattern.split('\n') for pattern in patterns]
notes = []
for pattern in patterns:
    reflection_row = get_reflection_row(pattern)
    reflection_column = get_reflection_column(pattern)
    if not reflection_row is None:
        notes.append(reflection_row*100)
    elif not reflection_column is None:
        notes.append(reflection_column)
    else:
        raise Exception()

total = sum(notes)
print("hello")