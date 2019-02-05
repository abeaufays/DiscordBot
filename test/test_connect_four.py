from connect_four import is_winning_move

import pytest

@pytest.fixture
def example_1():
    return [ ['X', 'X', 'X', 'X'], [],[],[],[],[],[]]

def test_is_winning_move(example_1):
    assert is_winning_move(example_1,'X', 0) == True
