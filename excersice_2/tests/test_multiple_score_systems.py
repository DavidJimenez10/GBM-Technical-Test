import pytest

from ..main import get_winner

def test_multiple_score_systems():
    """ Test if get_winner can handle multiple grand prixes score systems """
    assert get_winner(r'excersice_2/data/input_multiple_score_systems.txt') == "3\n3\n"