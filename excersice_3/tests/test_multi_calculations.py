import pytest

from ..main import calculate_minimum_jump

def test_multi_calculations():
    """ Test if get_winner can handle multiple grand prixes input """
    assert calculate_minimum_jump(5) == "1\n3\n2\n3\n4\n"