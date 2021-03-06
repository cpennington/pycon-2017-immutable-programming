import sys
from collections import Counter, namedtuple
from enum import Enum
from unittest import TestCase


class Player(Enum):
    X = "X"
    O = "O"
    NA = " "


def replace(tpl, idx, value):
    return tpl[:idx] + (value, ) + tpl[idx+1:]


class BoardState(namedtuple('_Board', ['board'])):
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
            return BoardState(
                replace(self.board, x, replace(self.board[x], y, self.player))
            )
        else:
            return self

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

BoardState.__new__.__defaults__ = (((Player.NA,)*3,)*3,)

class TestTicTacToe(TestCase):
    def test_basic_play(self):
        initial = BoardState()
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

# LOOP-START
def main():
    states = [BoardState()]
    while not states[-1].is_finished:
        print(states[-1])
        move = input(f"Player {states[-1].player.value}: "
                      "x y to move, u to undo, "
                      "gN to revert to move N)? ")
        if move == 'u':
            states.pop()
        elif move.startswith('g'):
            states = states[:int(move.replace('g','')) + 1]
        else:
            try:
                x, y = move.split()
                states.append(states[-1].do_move(int(x), int(y)))
            except:
                print("Invalid move")
# LOOP-END

    print("Game Over!")
    for state in states:
        print(state)


if __name__ == "__main__":
    sys.exit(main())