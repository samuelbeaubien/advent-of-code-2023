from gold2 import go_through_one_filter
import pytest

def test_go_through_one_filter():
    filter = [[52, 50, 48], [50, 98, 2]]
    source_ranges = [[55, 13], [79, 14]]
    expected = [[57, 13], [81, 14]]
    output = go_through_one_filter(filter, source_ranges)
    assert expected == output 

print("hello")