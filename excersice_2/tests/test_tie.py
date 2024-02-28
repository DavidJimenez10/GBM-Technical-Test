import pytest

from ..main import get_winner

def test_tie():
    """ Test if get_winner can handle multiple grand prixes input with tie """
    assert get_winner(r'excersice_2/data/input_tie.txt') == "3\n3\n1, 2, 3\n"