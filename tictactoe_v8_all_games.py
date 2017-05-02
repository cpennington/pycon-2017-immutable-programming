import sys
from collections import Counter, namedtuple
from enum import Enum
from unittest import TestCase
from random import randrange
from itertools import zip_longest, islice


class Player(Enum):
    X = "X"
    O = "O"
    NA = " "


class Undo(namedtuple('_Undo', ['count'])):
    def apply(self, boards):
        return boards[:-self.count]


class Move(namedtuple('_Move', ['x', 'y'])):
    def apply(self, boards):
        return boards + [boards[-1].do_move(self.x, self.y)]


class RevertTo(namedtuple('_RevertTo', ['idx'])):
    def apply(self, boards):
        return boards[:self.idx]


def replace(tpl, idx, value):
    return tpl[:idx] + (value, ) + tpl[idx+1:]


class Board():
    def __init__(self, board=None):
        if board:
            self._board = board
        else:
            self._board = tuple((Player.NA,)*3 for _ in range(3))

    @property
    def board(self):
        return self._board

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

    def do_move(self, x, y):
        if self.board[x][y] == Player.NA:
            return Board(
                replace(self.board, x, replace(self.board[x], y, self.player))
            )
        else:
            return self

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

        if all(all(col != Player.NA for col in row) for row in self.board):
            return True

        return False


class TestTicTacToe(TestCase):
    def test_basic_play(self):
        initial = Board()
        all_moves = [(x, y) for x in range(3) for y in range(3)]
        for (x0, y0) in all_moves:
            with self.subTest(x0=x0, y0=y0):
                after_first = initial.do_move(x0, y0)
                self.assertNotEqual(initial.player, after_first.player)
                self.assertNotEqual(initial.board, after_first.board)
                for (x1, y1) in all_moves:
                    with self.subTest(x1=x1, y1=y1):
                        after_second = after_first.do_move(x1, y1)
                        if x1 == x0 and y1 == y0:
                            self.assertEqual(after_first.player, after_second.player)
                            self.assertEqual(after_first.board, after_second.board)
                        else:
                            self.assertNotEqual(initial.player, after_first.player)
                            self.assertNotEqual(initial.board, after_first.board)


def depth_first(board=None):
    if board is None:
        board = Board()

    yield board

    for x in range(3):
        for y in range(3):
            next_board = board.do_move(x, y)
            if board != next_board:
                yield from depth_first(next_board)


def _breadth_first(board=None):
    if board is None:
        board = Board()

    yield [board]

    next_boards = (
        board.do_move(x, y)
        for x in range(3)
        for y in range(3)
    )

    next_boards = (
        _breadth_first(next) for next in next_boards if next != board
    )

    plies = zip_longest(*next_boards)

    for plies in plies:
        yield sum(plies, [])


def breadth_first(board=None):
    for ply in _breadth_first(board):
        yield from ply

def main():
    bf_boards = 0
    for board in breadth_first():
        bf_boards += 1

    df_boards = 0
    for board in depth_first():
        df_boards += 1

    print(bf_boards, df_boards)


if __name__ == "__main__":
    sys.exit(main())