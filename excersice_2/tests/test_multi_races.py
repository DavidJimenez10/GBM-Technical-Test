import pytest

from ..main import get_winner

def test_multi_races():
    """ Test if get_winner can handle multiple grand prixes races """
    assert get_winner(r'excersice_2/data/input_multi_races.txt') == "2, 4\n4\n"