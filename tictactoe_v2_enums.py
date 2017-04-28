import sys
from enum import Enum

# ENUM-START
class Player(Enum):
    X = "X"
    O = "O"
    NA = " "

    def next(self):
        next_players = {
            self.X: self.O,
            self.O: self.X,
        }
        return next_players[self]
# ENUM-END


# STORAGE-START
BOARD = [[Player.NA]*3 for _ in range(3)]
PLAYER = Player.X
# STORAGE-END


def format_board():
    return "--+---+--\n".join(
        " | ".join(play.value for play in row) + "\n"
        for row in BOARD
    )

# ACTION-START
def do_move():
    global PLAYER

    move = input(f"Player {PLAYER.value} move (x y)? ")
    x, y = move.split()
    if BOARD[int(x)][int(y)] == Player.NA:
        BOARD[int(x)][int(y)] = PLAYER
        PLAYER = PLAYER.next()
# ACTION-END


def is_finished():
    for row in BOARD:
        if row[0] != Player.NA and row[0] == row[1] == row[2]:
            return True

    for column in range(3):
        if BOARD[0][column] != Player.NA and BOARD[0][column] == BOARD[1][column] == BOARD[2][column]:
            return True

    if BOARD[0][0] != Player.NA and BOARD[0][0] == BOARD[1][1] == BOARD[2][2]:
        return True

    if BOARD[2][0] != Player.NA and BOARD[2][0] == BOARD[1][1] == BOARD[0][2]:
        return True

    return False


def main():
    while not is_finished():
        print(format_board())
        do_move()

    print("Game Over!")
    print(format_board())


if __name__ == "__main__":
    sys.exit(main())