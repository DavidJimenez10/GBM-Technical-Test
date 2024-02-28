import pytest

from ..main import is_palindrome

def test_allow_non_alpha():
    """ Test if is_palindrom can handle non-alphanumeric chars """
    assert is_palindrome('4. $ .4') is True
    assert is_palindrome('A$&a') is False