import pytest

from ..main import is_palindrome

def test_case_insensitive():
    """ Test if is_palindrom can handle letter case """
    assert is_palindrome('AnNa') is True
    assert is_palindrome('AnMa') is False
