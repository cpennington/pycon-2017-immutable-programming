import sys
from enum import Enum


class Player(Enum):
    X = "X"
    O = "O"
    NA = " "

    def next_player(self):
        next_players = {
            self.X: self.O,
            self.O: self.X,
        }
        return next_players[self]

# STORAGE-START
class TicTacToe():

    def __init__(self):
        self.board = [[Player.NA]*3 for _ in range(3)]
        self.player = Player.X
# STORAGE-END

    def __str__(self):
        return "--+---+--\n".join(
            " | ".join(play.value for play in row) + "\n"
            for row in self.board
        )

    # ACTION-START
    def do_move(self):
        move = input(f"Player {self.player.value} move (x y)? ")
        x, y = move.split()
        if self.board[int(x)][int(y)] == Player.NA:
            self.board[int(x)][int(y)] = self.player
            self.player = self.player.next_player()
    # ACTION-END

    # BUG-START
    def do_move_buggy(self):
        move = input(f"Player {self.player.value} move (x y)? ")
        x, y = move.split()
        if self.board[int(x)][int(y)] == Player.NA:
            self.board[int(x)][int(y)] = self.player
        self.player = self.player.next_player()
    # BUG-END

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


# LOOP-START
def main():
    game = TicTacToe()
    while not game.is_finished():
        print(game)
        game.do_move()

    print("Game Over!")
    print(game)
# LOOP-END


if __name__ == "__main__":
    sys.exit(main())