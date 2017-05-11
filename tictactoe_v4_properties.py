import sys
from collections import Counter
from enum import Enum
from unittest import TestCase


# ENUM-START
class Player(Enum):
    X = "X"
    O = "O"
    NA = " "
# ENUM-END


# STORAGE-START
class Board():
    def __init__(self):
        self.board = [[Player.NA]*3]*3
# STORAGE-END

    # PROPERTY-START
    @property
    def player(self):
        plays = Counter(sum(self.board, []))
        if plays[Player.O] < plays[Player.X]:
            return Player.O
        else:
            return Player.X
    # PROPERTY-END

    def __str__(self):
        return "--+---+--\n".join(
            " | ".join(play.value for play in row) + "\n"
            for row in self.board
        )

    # ACTION-START
    def do_move(self, x, y):
        if self.board[x][y] == Player.NA:
            self.board[x][y] = self.player
    # ACTION-END

    @property
    def is_finished(self):
        for row in self.board:
            if row[0] != Player.NA and row[0] == row[1] == row[2]:
                return True

        for column in range(3):
            if self.board[0][column] != Player.NA and self.board[0][column] == self.board[1][column] == self.board[2][column]:
                return True

        if self.board[0][0] != Player.NA and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[2][0] != Player.NA and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return True

        return False

class BoardCorrected():
    # FIXED-STORAGE-START
    def __init__(self):
        self.board = [[Player.NA]*3 for _ in range(3)]
    # FIXED-STORAGE-END

class TestTicTacToe(TestCase):
    def setUp(self):
        self.game = Board()

    # TEST-START
    def test_basic_play(self):
        self.assertEqual(self.game.player, Player.X)
        self.game.do_move(0, 0)
        self.assertEqual(self.game.board[0][0], Player.X)
        self.assertEqual(self.game.player, Player.O)
        self.game.do_move(0, 1)
        self.assertEqual(self.game.board[0][1], Player.O)
        self.assertEqual(self.game.player, Player.X)
    # TEST-END

    def test_same_move(self):
        self.assertEqual(self.game.player, Player.X)
        self.game.do_move(0, 0)
        self.assertEqual(self.game.player, Player.O)
        self.game.do_move(0, 0)
        self.assertEqual(self.game.player, Player.O)

    # FAILED-TEST-START
    def test_game_end(self):
        self.assertFalse(self.game.is_finished)
        self.game.do_move(0, 0)
        self.assertFalse(self.game.is_finished)
    # FAILED-TEST-END
        self.game.do_move(0, 1)
        self.assertFalse(self.game.is_finished)
        self.game.do_move(1, 0)
        self.assertFalse(self.game.is_finished)
        self.game.do_move(1, 1)
        self.assertFalse(self.game.is_finished)
        self.game.do_move(2, 0)
        self.assertTrue(self.game.is_finished)

    # DEEP-TEST-START
    def test_moves_made(self):
        before = {
            (x, y, self.game.board[x][y])
            for x in range(3)
            for y in range(3)
        }
        self.game.do_move(0, 0)
        after = {
            (x, y, self.game.board[x][y])
            for x in range(3)
            for y in range(3)
        }
        self.assertEqual(after - before, {(0, 0, Player.X)})
        self.assertEqual(before - after, {(0, 0, Player.NA)})
    # DEEP-TEST-END



# LOOP-START
def main():
    game = Board()
    while not game.is_finished:
        print(game)

        move = input(f"Player {game.player.value} move (x y)? ")
        x, y = move.split()

        game.do_move(int(x), int(y))

    print("Game Over!")
    print(game)
# LOOP-END


if __name__ == "__main__":
    sys.exit(main())