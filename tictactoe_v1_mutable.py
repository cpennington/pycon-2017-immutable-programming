import sys

# STORAGE-START
BOARD = [[" "]*3 for _ in range(3)]
PLAYER = "X"
# STORAGE-END


def format_board():
    return "--+---+--\n".join(
        " | ".join(row) + "\n"
        for row in BOARD
    )

# ACTION-START
def do_move():
    global PLAYER

    move = input(f"Player {PLAYER} move (x y)? ")
    x, y = move.split()
    if BOARD[int(x)][int(y)] == " ":
        BOARD[int(x)][int(y)] = PLAYER
        PLAYER = "X" if PLAYER == "O" else "O"
# ACTION-END

def is_finished():
    for row in BOARD:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    for column in range(3):
        if BOARD[0][column] != " " and BOARD[0][column] == BOARD[1][column] == BOARD[2][column]:
            return True

    if BOARD[0][0] != " " and BOARD[0][0] == BOARD[1][1] == BOARD[2][2]:
        return True

    if BOARD[2][0] != " " and BOARD[2][0] == BOARD[1][1] == BOARD[0][2]:
        return True

    return False

# LOOP-START
def main():
    while not is_finished():
        print(format_board())
        do_move()

    print("Game Over!")
    print(format_board())
# LOOP-END


if __name__ == "__main__":
    sys.exit(main())