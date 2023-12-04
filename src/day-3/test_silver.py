import pytest

from silver import Schematic as Schematic

def test_is_special_char():
    false_inputs = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for char in false_inputs:
        assert not Schematic._is_special_char(char)
    true_inputs = ['-', '|', '\\', '/', '+', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '~', '`']
    for char in true_inputs:
        assert Schematic._is_special_char(char)

def test_is_part_number_one_line():
    # One line:
    inputs = [
        ['', 0, 0, 0],
        ['.', 0, 0, 0],
        ['1.', 0, 0, 0],
        ['.1', 0, 1, 1],
        ['1%', 0, 0, 0],
        ['%1', 0, 1, 1],
        ['1//', 0, 0, 0],
        ['//1', 0, 1, 1]
    ]
    outputs = [
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True
    ]
    for input, output in zip(inputs, outputs):
        sch = Schematic(input[0])
        assert output == sch.is_part_number(sch, input[1], input[2], input[3])

def test_is_part_number_two_lines():
    inputs = [
        [
            [
                '1.',
                '..'
            ],
            0, 0, 0],
        [
            [
                '.1',
                '.1'
            ],
            0, 1, 1],
        [
            [
                '1',
                '.%'
            ],
            0, 0, 0],
        [
            [
                '.1',
                '%.'
            ],
            0, 1, 1],
        [
            [
                '1.',
                './/'
            ],
            0, 0, 0],
        [
            [
                '.1',
                '//.'
            ],
            0, 1, 1],
        [
            [
                '.1.',
                '#..'
            ],
            0, 1, 1],
        [
            [
                '.1.',
                '.#.'
            ],
            0, 1, 1],    
        [
            [
                '.1.',
                '..#'
            ],
            0, 1, 1],
        [
            [
                '..1',
                '.#.'
            ],
            0, 2, 2],
        [
            [
                '1..',
                '.#.'
            ],
            0, 1, 1],    
        [
            [
                '1..',
                '#..'
            ],
            0, 0, 0],
        [
            [
                '1..',
                '..#'
            ],
            0, 0, 0]
    ]
    outputs = [
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False
    ]
    for input, output in zip(inputs, outputs):
        sch = Schematic(input[0])
        assert output == sch.is_part_number(sch, input[1], input[2], input[3])

def test_get_NumPos_in_line():
    input = """
    *..
    .1.
    ...
    .11.
    ...*
    ..*..
    .111.
    .
    .111.
    .*...
    1
    """
    output = [
        1, 11, 111, 111, 1
    ]
    sch = Schematic(input)
    num_pos = sch.get_NumPos_in_line(sch, 0)
    