from typing import List
import re

class NumPos:
    """Contains a number and its position in a 2x2 grid
    """
    def __init__(self, num: int, line_num: int, start_index: int, end_index: int, is_part_num: bool):
        """Constructor for NumPos

        Args:
            num: The number
            line_num: The line in which the number is.
            start_index: The index of the first character of the number.
            end_index: The index of the last character of the number.
            is_part_num: Is a part number
        """
        self.num = num
        self.line_num = line_num
        self.start_pos = start_index
        self.end_pos = end_index
        self.is_part_num = is_part_num

    def __str__(self):
        return f'{self.num}, Line: {self.line_num}, [{self.start_pos}, {self.end_pos}], Is Part: {self.is_part_num}'

class Schematic:
    def __init__(self, lines: list[str]):
        self.lines = lines
        self.grid = [list(line) for line in lines]

    @classmethod
    def _is_special_char(self, char: str) -> bool:
        """Check if character is a special character.
        A special character is a character that is not a digit or a dot.

        Args:
            line: The line
            index: The index

        Returns:
            True if character is a special character, False otherwise
        """
        if char == '.' or char.isdigit():
            return False
        else:
            return True                                                             


    @classmethod
    def is_part_number(cls, schematic, line_num: int, start_index: int, end_index: int) -> bool:
        """Check if number is part number
        A number is represented by its start index and its end index.
        A number is a part number if has at least one special character adjacent
        to it.

        Args:
            schematic: The schematic
            line_num: The line number
            start_index: The start index
            end_index: The end index
        
        Returns:
            True if number is a part number, False otherwise
        """
        # Iterate through each lines, the previous, the current and the next
        line_numbers = [line_num - 1, line_num, line_num + 1]
        for cur_line_num in line_numbers:
            if cur_line_num >= 0 and cur_line_num < len(schematic.lines):
                cur_line = str(schematic.lines[cur_line_num])
                # Check the extremities
                if (start_index-1) >= 0:
                    char = cur_line[start_index-1]
                    if cls._is_special_char(char):
                        return True
                if (end_index+1) < len(cur_line):
                    char = cur_line[end_index+1]
                    if cls._is_special_char(char):
                        return True  
                # Check the middle
                middle = cur_line[start_index:end_index+1]
                middle_chars = list(middle)
                for char in middle_chars:
                    if cls._is_special_char(char):
                        return True
        return False

    @classmethod
    def get_NumPos_in_line(cls, schematic, line_num: int):
        """Returns a list of NumPos objects that are in a line.

        Args:
            schematic : The line to search
            grid : The grid to search in.
        """
        # Copy line
        line = str(schematic.lines[line_num])
        sub_strings = re.split('(\d+)', line)
        # line.split('.')
        nums = []
        for sub_string in sub_strings:
            if sub_string.isdigit():
                nums.append(int(sub_string))
        # Get NumPos objects
        num_pos = []
        for num in nums:
            start_index = line.find(str(num))
            end_index = start_index + len(str(num)) - 1
            is_part_num = cls.is_part_number(schematic, line_num, start_index, end_index)
            num_pos.append(NumPos(num, line_num, start_index, end_index, is_part_num))
            line.replace(str(num), '.'*len(str(num)), 1)
        return num_pos
        
    @classmethod
    def get_NumPos_in_grid(cls, schematic) -> list[NumPos]:
        """Returns a list of NumPos objects that are in a grid

        Args:
            gschematicrid: The schematic to search in
        """
        num_pos = []
        for line_num in range(0, len(schematic.lines)):
            cur_line = schematic.lines[line_num]
            cur_num_pos = cls.get_NumPos_in_line(schematic, line_num)
            num_pos.append(cur_num_pos)
        return num_pos







# ### SCRIPT ###

file = open('src/day-3/input.txt', 'r')
lines_orig = file.readlines()
lines = [line[:-1] for line in lines_orig]
sch = Schematic(lines)
num_pos_list = Schematic.get_NumPos_in_grid(sch)
total = 0
for num_pos_line in num_pos_list:
    for line_number in num_pos_line:
        if line_number.is_part_num:
            total += line_number.num

ss = ''
for line_number, num_pos_line, line  in zip(range(0, len(sch.lines)), num_pos_list, sch.lines):
    s = f"L.{line_number+1}: {line}\n\t"
    for cur_num_pos in num_pos_line:
        s += f'[{cur_num_pos.num}|{cur_num_pos.is_part_num}], '
    s += '\n'
    print(s)
    ss += s
# Write ss to a file called test
file = open('test_output.txt', 'w')
file.write(ss)

print(total)




# Test:

# lines = [
# '...*......',
# '..35..633.',
# '......#...'
# ]
# grid_obj = Grid(lines)
# num_pos = get_NumPos_in_grid(grid_obj)


# lines = [
# '617*......'
# ]
# grid_obj = Grid(lines)
# num_pos = get_NumPos_in_grid(grid_obj)




print ("hello")

