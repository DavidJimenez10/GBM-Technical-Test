import pytest

from ..main import is_palindrome

def test_allow_number():
    """ Test if is_palindrom can handle numbers """
    assert is_palindrome('1221') is True
    assert is_palindrome('1231') is False