import sys
from collections import Counter, namedtuple
from enum import Enum
from unittest import TestCase


class Player(Enum):
    X = "X"
    O = "O"
    NA = " "


# REPLACE-START
def replace(tpl, idx, value):
    return tpl[:idx] + (value, ) + tpl[idx+1:]
# REPLACE-END

class Board(namedtuple('_Board', ['board'])):
    @property
    def player(self):
        plays = Counter(sum(self.board, ()))
        if plays[Player.O] < plays[Player.X]:
            return Player.O
        else:
            return Player.X

    def __str__(self):
        return "--+---+--\n".join(
            " | ".join(play.value for play in row) + "\n"
            for row in self.board
        )

    # ACTION-START
    def do_move(self, x, y):
        if self.board[x][y] == Player.NA:
            new_row = replace(self.board[x], y, self.player)
            new_board = replace(self.board, x, new_row)
            return Board(new_board)
        else:
            return self
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

    def __sub__(self, other):
        diff = set()
        for x in range(3):
            for y in range(3):
                if self.board[x][y] != other.board[x][y]:
                    diff.add((x, y, self.board[x][y]))
        return diff

Board.__new__.__defaults__ = (((Player.NA,)*3,)*3,)

class TestTicTacToe(TestCase):
    # TEST-START
    def test_moves_made(self):
        before = Board()
        after = before.do_move(0, 0)
        self.assertEqual(after - before, {(0, 0, Player.X)})
        self.assertEqual(before - after, {(0, 0, Player.NA)})
    # TEST-END
    def test_basic_play(self):
        initial = Board()
        all_moves = [(x, y) for x in range(3) for y in range(3)]

        for (x0, y0) in all_moves:
            with self.subTest(x0=x0, y0=y0):
                after_first = initial.do_move(x0, y0)
                self.assertEqual(
                    after_first - initial,
                    {(x0, y0, Player.X)}
                )
                # TEST-2-START
                for (x1, y1) in all_moves:
                    with self.subTest(x1=x1, y1=y1):
                        after_second = after_first.do_move(x1, y1)
                        if x1 == x0 and y1 == y0:
                            self.assertEqual(after_second - after_first, set())
                        else:
                            self.assertEqual(
                                after_second - after_first,
                                {(x1, y1, Player.O)}
                            )
                # TEST-2-END

# LOOP-START
def main():
    board = Board()
    while not board.is_finished:
        print(board)
        move = input(f"Player {board.player.value} (x y)? ")
        x, y = move.split()
        x = int(x)
        y = int(y)

        board = board.do_move(x, y)
# LOOP-END

    print("Game Over!")
    print(board)


if __name__ == "__main__":
    sys.exit(main())