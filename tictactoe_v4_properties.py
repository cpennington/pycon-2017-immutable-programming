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


# INTRO-START
class Board():
    def __init__(self):
        self.board = [[Player.NA]*3]*3]

    def do_move(self, x, y):
        if self.board[x][y] == Player.NA:
            self.board[x][y] = self.player
# INTRO-END

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
        self.board = Board()

    # TEST-START
    def test_basic_play(self):
        # Check the current player
        self.assertEqual(self.board.player, Player.X)
        self.board.do_move(0, 0)
        # Check that the move worked
        self.assertEqual(self.board.board[0][0], Player.X)
        # Check that the player changed
        self.assertEqual(self.board.player, Player.O)
    # TEST-END

    def test_same_move(self):
        self.assertEqual(self.board.player, Player.X)
        self.board.do_move(0, 0)
        self.assertEqual(self.board.player, Player.O)
        self.board.do_move(0, 0)
        self.assertEqual(self.board.player, Player.O)

    # FAILED-TEST-START
    def test_game_end(self):
        self.assertFalse(self.board.is_finished)
        self.board.do_move(0, 0)
        self.assertFalse(self.board.is_finished)
    # FAILED-TEST-END
        self.board.do_move(0, 1)
        self.assertFalse(self.board.is_finished)
        self.board.do_move(1, 0)
        self.assertFalse(self.board.is_finished)
        self.board.do_move(1, 1)
        self.assertFalse(self.board.is_finished)
        self.board.do_move(2, 0)
        self.assertTrue(self.board.is_finished)

    # DEEP-TEST-START
    def test_moves_made(self):
        # Store the state of the board before a move
        before = {(x, y, self.board.board[x][y]) for (x, y) in ALL_MOVES}

        # Make a single move
        self.board.do_move(0, 0)

        # Store the state of the board after the move
        after = {(x, y, self.board.board[x][y]) for (x, y) in ALL_MOVES}

        # Compare the state before and after
        self.assertEqual(after - before, {(0, 0, Player.X)})
        self.assertEqual(before - after, {(0, 0, Player.NA)})
    # DEEP-TEST-END


ALL_MOVES = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# DEPTH-FIRST-START
def depth_first(board=None):
    if board is None:
        board = Board()

    yield board

    for x, y in ALL_MOVES:
        if board.board[x][y] != Player.NA:
            board.do_move(x, y)
            try:
                yield from depth_first(board)
            finally:
                board.board[x][y] = Player.NA
# DEPTH-FIRST-END

# DEPTH-COPY-START
def depth_first(board=None):
    if board is None:
        board = Board()

    yield board

    for x, y in ALL_MOVES:
        if board.board[x][y] != Player.NA:
            old_board = [list(board.board[x]) for x in range(3)]
            board.do_move(x, y)
            try:
                yield from depth_first(board)
            finally:
                board.board = old_board
# DEPTH-COPY-END

# LOOP-START
def main():
    board = Board()
    while not board.is_finished:
        print(board)

        move = input(f"Player {board.player.value} move (x y)? ")
        x, y = move.split()

        board.do_move(int(x), int(y))
# LOOP-END

    print("Game Over!")
    print(board)


if __name__ == "__main__":
    sys.exit(main())