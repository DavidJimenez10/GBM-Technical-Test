import pytest

from ..main import get_winner

def test_multi_calculations():
    """ Test if get_winner can handle multiple grand prixes input """
    assert get_winner(r'excersice_2/data/input_multi_calculations.txt') == "3\n3\n1, 2, 3\n2, 4\n4\n3\n3\n"