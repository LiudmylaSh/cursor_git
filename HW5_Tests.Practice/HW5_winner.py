import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_winner_row_ind(self):
        self.game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(4, 'X'))
        self.assertTrue(self.game.winner(5, 'X'))
        self.game.board = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(0, 'O'))
        self.assertTrue(self.game.winner(1, 'O'))
        self.assertTrue(self.game.winner(2, 'O'))

    def test_winner_col_ind(self):
        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.game.board = [' ', 'X', ' ', ' ', 'O', ' ', ' ', 'O', ' ']
        self.assertFalse(self.game.winner(1, 'O'))

    def test_winner_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(0, 'X'))
        self.game.board = [' ', ' ', 'O', ' ', 'O', ' ', 'O', ' ', ' ']
        self.assertTrue(self.game.winner(2, 'O'))


if __name__ == '__main__':
    unittest.main()