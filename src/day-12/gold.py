from typing import List

RECORD = {}

class SubProblem:
    def __init__(self, parent, field: str, groups: List[int]):
        self.parent = parent
        self.field = field
        self.groups = groups

    def is_field_long_enough(self):
        minimum_len = sum(self.groups) + len(self.groups) - 1
        return len(self.field) >= minimum_len

    def get_record_key(self):
        return f"F:{self.field}-G:{str(self.groups)}"

    def is_base_case(self):
        return self.field == "" or self.groups == []
    
    def get_val_base_case(self):
        if self.is_base_case():
            if self.field == "":
                if self.groups == []:
                    return 1
                else:
                    return 0
            else:
                if all([(c == '.' or c == '?') for c in self.field]):
                    return 1
                else:
                    return 0
        else:
            raise Exception("Not a base case")
        
    def is_val_available(self):
        return self.is_base_case() or self.get_record_key() in RECORD

    def get_val(self):
        if self.is_val_available():
            if self.is_base_case():
                return self.get_val_base_case()
            return RECORD[self.get_record_key()]
        else:
            raise Exception("Value not available")

    def _get_sub_problem_if_next_is_operational(self):
        if self.field[0] == '.' or self.field[0] == '?':
            new_sub_problem = SubProblem(self, self.field[1:], self.groups)
            if new_sub_problem.is_field_long_enough():
                return new_sub_problem
        return InvalidSubProblem(self)
        
    def _get_sub_problem_if_next_is_damaged(self):
        cur_group = self.groups[0]
        new_groups = self.groups[1:]
        damaged_len = cur_group
        if len(self.field) == damaged_len:
            if all([(c == '#' or c == '?') for c in self.field]):
                new_sub_problem = SubProblem(self,  self.field[damaged_len:], new_groups)
                if new_sub_problem.is_field_long_enough():
                    return new_sub_problem
            return InvalidSubProblem(self)
        # Need a dot or a question mark after the damaged part
        damaged_len_with_dot = cur_group +1
        if len(self.field) >= damaged_len_with_dot:
            damaged_part = self.field[:damaged_len]
            following_character = self.field[damaged_len]
            if (
                all([(c == '#' or c == '?') for c in damaged_part]) and 
                (following_character == '.' or following_character == '?')
            ):
                new_sub_problem = SubProblem(self, self.field[damaged_len_with_dot:], new_groups)
                if new_sub_problem.is_field_long_enough():
                    return new_sub_problem
            return InvalidSubProblem(self)
        return InvalidSubProblem(self)
        
    def compute_and_get_next_sub_problem(self):
        next_sub_problem_operational = self._get_sub_problem_if_next_is_operational()
        next_sub_problem_damaged = self._get_sub_problem_if_next_is_damaged()
        if not next_sub_problem_operational.is_val_available():
            return next_sub_problem_operational
        elif not next_sub_problem_damaged.is_val_available():
            return next_sub_problem_damaged
        else:
            next_sub_problem_operational_val = next_sub_problem_operational.get_val()
            next_sub_problem_damaged_val = next_sub_problem_damaged.get_val()
            RECORD[self.get_record_key()] = next_sub_problem_operational_val + next_sub_problem_damaged_val
            return self


class InvalidSubProblem(SubProblem):
        def __init__(self, parent) -> None:
            super().__init__(parent, None, None)
        def get_record_key(self):
            raise Exception("Invalid sub problem")
        def is_base_case(self):
            return False
        def is_val_available(self):
            return True
        def get_val(self):
            return 0


def get_num_possibilities_with_tree(initial_sub_problem: SubProblem) -> int:
    cur_sub_problem = initial_sub_problem
    while not initial_sub_problem.is_val_available():
        if cur_sub_problem.is_val_available():
            cur_sub_problem = cur_sub_problem.parent
        else:
            cur_sub_problem = cur_sub_problem.compute_and_get_next_sub_problem()
    total_possibilities = initial_sub_problem.get_val()
    return total_possibilities

def unfold_field(field: str) -> str:
    unfolded_field = ""
    for _ in range(5):
        unfolded_field += field
        unfolded_field += '?'
    unfolded_field = unfolded_field[:-1]
    return unfolded_field

def unfold_groups(groups: List[int]) -> List[int]:
    unfolded_groups = []
    for _ in range(5):
        unfolded_groups += groups
    return unfolded_groups



### SCRIPT ###

file = open("src/day-12/input.txt")
lines = file.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [line.split(' ') for line in lines]
fields = [line[0] for line in lines]
groups_list = [[int(num) for num in list(line[1].split(','))] for line in lines]

total_possibilities =[]
for field, groups in zip(fields, groups_list):
    unfolded_field = unfold_field(field)
    unfolded_groups = unfold_groups(groups)
    sub_problem = SubProblem(None, unfolded_field, unfolded_groups)
    total_possibilities.append(get_num_possibilities_with_tree(sub_problem))

num_possibilities = sum(total_possibilities)

print(total_possibilities)
print("Hello")