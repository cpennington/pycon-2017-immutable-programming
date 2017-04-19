import sys

BOARD = [[" "]*3 for _ in range(3)]
PLAYER = "X"

def print_board():
    for ri, row in enumerate(BOARD):
        for ci, column in enumerate(row):
            print(column, end='')
            if ci != 2:
                print (' | ', end='')
        print('')
        if ri != 2:
            print('--+---+--')


def do_move():
    global PLAYER

    move = input(f"Player {PLAYER} move (x y)? ")
    x, y = move.split()
    BOARD[int(x)][int(y)] = PLAYER
    PLAYER = "X" if PLAYER == 'Y' else 'Y'


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


def main():
    while not is_finished():
        print_board()
        do_move()

    print("Game Over!")
    print_board()


if __name__ == "__main__":
    sys.exit(main())