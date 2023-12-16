from typing import List

class SubProblem:
    def __init__(self, parent, field: str, groups: List[int]):
        self.parent = parent
        self.field = field
        self.groups = groups

    # def __init__(self, parent, key: str):
    #     self.parent = parent
    #     self.field, self.groups = decode_record_key(key)

    # def get_record_key(self):
    #     return f"{self.field}-{str(self.groups)}"

RECORD = {}

def get_record_key(field: str, groups: List[int]):
    return f"{field}-{str(groups)}"

def decode_record_key(key: str):
    field, group = key.split('-')
    group = [int(val) for val in group[1:-1].split(',')]
    return field, group

def get_input_key_if_next_is_operational(field: str, groups: List[int]) -> str:
    if field[0] == '.' or field[0] == '?':
        return get_record_key(field[1:], groups)
    else:
        return None
    
def get_input_key_if_next_is_damaged(field: str, groups: List[int]) -> str:
    cur_group = groups[0]
    new_groups = groups[1:]
    if field[0] == '#' or field[0] == '?':
        necessary_len = cur_group + 1
        if all([(c == '#' or c == '?') for c in field[:necessary_len]]):
            return get_record_key(field[necessary_len:], new_groups)
        else:
            return None
    else:
        return None
    
def check_base_case(field: str, groups: List[int]) -> int:
    if field == "":
        if groups == []:
            return 1
        else:
            return 0
    elif groups == []:
        if all([(c == '.' or c == '?') for c in field]):
            return 1
        else:
            return 0
    else:
        return None
    
def get_num_possibilities_with_tree(initial_field: str, initial_groups: List[int]) -> int:
    initial_sub_problem = SubProblem(None, initial_field, initial_groups)
    initial_key = get_record_key(initial_field, initial_groups)
    cur_sub_problem = initial_sub_problem
    while not initial_key in RECORD:
        cur_key = get_record_key(cur_sub_problem.field, cur_sub_problem.groups)
        # Check base case if already computed
        if cur_key in RECORD:
            cur_sub_problem = RECORD[cur_key].parent
            continue
        # Check base case if not computed yet
        base_case_result = check_base_case(cur_sub_problem.field, cur_sub_problem.groups)
        if base_case_result != None:
            RECORD[cur_key] = base_case_result
            cur_sub_problem = cur_sub_problem.parent
            continue
        # This sub problem is a parent. Check if its children are already computed or compute children
        next_key_operational = get_input_key_if_next_is_operational(cur_sub_problem.field, cur_sub_problem.groups)
        next_key_damaged = get_input_key_if_next_is_damaged(cur_sub_problem.field, cur_sub_problem.groups)
        # Check all the cases if the key of one child is None
        if next_key_operational is None or next_key_damaged is None:
            if next_key_operational is None and next_key_damaged is None:
                RECORD[cur_key] = 0
                cur_sub_problem = cur_sub_problem.parent
            elif next_key_operational is None:
                if next_key_damaged in RECORD:
                    RECORD[cur_key] = RECORD[next_key_damaged]
                    cur_sub_problem = cur_sub_problem.parent
                else:
                    cur_sub_problem = SubProblem(cur_sub_problem, *decode_record_key(next_key_damaged))
                continue
            else:
                if next_key_operational in RECORD:
                    RECORD[cur_key] = RECORD[next_key_operational]
                    cur_sub_problem = cur_sub_problem.parent
                else:
                    cur_sub_problem = SubProblem(cur_sub_problem, *decode_record_key(next_key_operational))
                continue
        # No None keys
        if next_key_operational in RECORD and next_key_damaged in RECORD:
            RECORD[cur_key] = RECORD[next_key_operational] + RECORD[next_key_damaged]
            cur_sub_problem = cur_sub_problem.parent
        elif next_key_operational in RECORD:
            cur_sub_problem = SubProblem(cur_sub_problem, *decode_record_key(next_key_damaged))
        else:
            cur_sub_problem = SubProblem(cur_sub_problem, *decode_record_key(next_key_operational))

    return RECORD[initial_key]

### SCRIPT ###

file = open("src/day-12/example.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [line.split(' ') for line in lines]
fields = [line[0] for line in lines]
groups_list = [[int(num) for num in list(line[1].split(','))] for line in lines]

total_possibilities = 0
for field, groups in zip(fields, groups_list):
    total_possibilities += get_num_possibilities_with_tree(field, groups)

print(total_possibilities)
print("Hello")