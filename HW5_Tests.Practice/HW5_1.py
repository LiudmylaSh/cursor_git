#1. Create a the same tests as tic-tac/test_game but with pytest.
import pytest
from game import TicTacToe

def setup_module(module):
    global game_test
    game_test = TicTacToe()
    game_test.board[4] = "X"


def test_available_moves():
        assert not (4 in game_test.available_moves())

def test_make_move():
        assert not (game_test.make_move(4, "X"))
        assert (game_test.make_move(5, "X"))
        assert (game_test.board[5] != " ")
