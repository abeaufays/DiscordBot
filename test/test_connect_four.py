from connect_four import is_winning_move
from connect_four import get_string
import pytest

@pytest.fixture
def empty():
    return [[],[],[],[],[],[],[]]

@pytest.fixture
def first_column_point():
    return [ ['X', 'X', 'X', 'X'], [],[],[],[],[],[]]

@pytest.fixture
def row_point():
    return [ ['O', 'O', 'X'], ['O','O','X','O'],['O','O','X'],['O','O','X'],['O','O','O'],[],[]]


@pytest.fixture
def diag_simple():
    return [ ['X'], ['X','X'], ['O','O','X'],['O','O','O','X'],[],[],[]]

@pytest.fixture
def reverse_diag():
    return [['O','X'],['X'],['O','O','O','X'],['O','O','X','O'],['O','X'],['X'],[]]

@pytest.fixture
def random():
    return [['X','O','O','X'],['X','X','O','O','X'],['O','O','X','X','O'],['O','O','O','O','O'],['X','X','X','O','O'],['O','O','O','X'],['O','O']]

@pytest.fixture
def diag_trunced():
    return [['O','X'],['O','O','X'],['O','O','O','X'],['O','O','O','O','X'],[],[],[]]

@pytest.fixture
def reverse_diag_trunced():
    return [[],[],['X'],['O','O','O','O','X'],['O','O','O','X'],['O','O','X'],['O','X']]

def test_is_winning_move_column(first_column_point):
    assert is_winning_move(first_column_point,'X', 0) == True
    assert is_winning_move(first_column_point,'X', 1) == False
    assert is_winning_move(first_column_point,'X', 2) == False
    assert is_winning_move(first_column_point,'X', 3) == False
    assert is_winning_move(first_column_point,'X', 4) == False
    assert is_winning_move(first_column_point,'O', 0) == False


def test_is_winning_move_row(row_point):
    assert is_winning_move(row_point, 'X', 0) == True
    assert is_winning_move(row_point, 'X', 1) == False
    assert is_winning_move(row_point, 'X', 2) == True
    assert is_winning_move(row_point, 'X', 3) == True
    assert is_winning_move(row_point, 'X', 4) == True

def test_is_winning_move_diag_simple(diag_simple):
    assert is_winning_move(diag_simple,'X',0) == True
    assert is_winning_move(diag_simple,'X',1) == True
    assert is_winning_move(diag_simple,'X',2) == True
    assert is_winning_move(diag_simple,'X',3) == True
    assert is_winning_move(diag_simple,'X',4) == False
    assert is_winning_move(diag_simple,'X',5) == False

def test_is_winning_move_diag_reverse(reverse_diag):
    assert is_winning_move(reverse_diag,'X',0) == False
    assert is_winning_move(reverse_diag,'X',1) == False
    assert is_winning_move(reverse_diag,'X',2) == True
    assert is_winning_move(reverse_diag,'X',3) == False
    assert is_winning_move(reverse_diag,'X',4) == True
    assert is_winning_move(reverse_diag,'X',5) == True
    assert is_winning_move(reverse_diag,'X',6) == False

def test_is_winning_move_random(random):
    assert is_winning_move(random,'X',0) == False
    assert is_winning_move(random,'X',1) == False
    assert is_winning_move(random,'X',2) == False
    assert is_winning_move(random,'X',3) == False
    assert is_winning_move(random,'X',4) == False
    assert is_winning_move(random,'X',5) == False
    assert is_winning_move(random,'X',6) == False

def test_is_winning_move_diag_trunced(diag_trunced):
    assert is_winning_move(diag_trunced,'X',0) == True
    assert is_winning_move(diag_trunced,'X',1) == True
    assert is_winning_move(diag_trunced,'X',2) == True
    assert is_winning_move(diag_trunced,'X',3) == True
    assert is_winning_move(diag_trunced,'X',4) == False
    assert is_winning_move(diag_trunced,'X',5) == False
    assert is_winning_move(diag_trunced,'X',6) == False

def test_is_winning_move_reverse_diag_trunced(reverse_diag_trunced):
    assert is_winning_move(reverse_diag_trunced,'X',0) == False
    assert is_winning_move(reverse_diag_trunced,'X',1) == False
    assert is_winning_move(reverse_diag_trunced,'X',2) == False
    assert is_winning_move(reverse_diag_trunced,'X',3) == True
    assert is_winning_move(reverse_diag_trunced,'X',4) == True
    assert is_winning_move(reverse_diag_trunced,'X',5) == True
    assert is_winning_move(reverse_diag_trunced,'X',6) == True


def test_string_empty(empty):
    expected = ("       \n"
                "       \n"
                "       \n"
                "       \n"
                "       \n"
                "       \n")
    assert get_string(empty," ") == expected
def test_string_first_column_point(first_column_point):
    expected = ("       \n"
                "       \n"
                "X      \n"
                "X      \n"
                "X      \n"
                "X      \n")
    assert get_string(first_column_point," ") == expected
def test_string_row_point(row_point):
    expected = ("       \n"
                "       \n"
                " O     \n"
                "XXXXO  \n"
                "OOOOO  \n"
                "OOOOO  \n")
    assert get_string(row_point," ") == expected
def test_string_diag_simple(diag_simple):
    expected = ("       \n"
                "       \n"
                "   X   \n"
                "  XO   \n"
                " XOO   \n"
                "XXOO   \n")
    assert get_string(diag_simple," ") == expected
def test_string_reverse_diag(reverse_diag):
    expected = ("       \n"
                "       \n"
                "  XO   \n"
                "  OX   \n"
                "X OOX  \n"
                "OXOOOX \n")
    assert get_string(reverse_diag," ") == expected
def test_string_random(random):
    expected = ("       \n"
                " XOOO  \n"
                "XOXOOX \n"
                "OOXOXO \n"
                "OXOOXOO\n"
                "XXOOXOO\n")
    assert get_string(random," ") == expected
def test_string_diag_trunced(diag_trunced):
    expected = ("       \n"
                "   X   \n"
                "  XO   \n"
                " XOO   \n"
                "XOOO   \n"
                "OOOO   \n")
    assert get_string(diag_trunced," ") == expected
def test_string_reverse_diag_trunced(reverse_diag_trunced):
    expected = ("       \n"
                "   X   \n"
                "   OX  \n"
                "   OOX \n"
                "   OOOX\n"
                "  XOOOO\n")
    assert get_string(reverse_diag_trunced," ") == expected