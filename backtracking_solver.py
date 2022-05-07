start_board = [
    [9, 0, 0, 8, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 9, 6, 0, 3, 8, 7],
    [0, 0, 0, 0, 3, 8, 0, 2, 4],
    [0, 1, 0, 0, 0, 0, 0, 9, 0],
    [2, 6, 0, 5, 9, 0, 0, 0, 0],
    [5, 9, 1, 0, 8, 7, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 9, 0, 0, 3]
]

count = 0


def show_board(board):
    for row in range(9):
        for column in range(9):
            print(f"{board[row][column]}", end='')
            if (column+1) % 3 == 0 and column != 0 and column != 8:
                print(' | ', end='')
            else:
                print(' ', end='')
        print("")
        if (row+1) % 3 == 0 and row != 8:
            print('- - - - - - - - - - -')


def find_empty(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return None


def check_valid(board, value, pos):
    row = pos[0]
    column = pos[1]
    if board[row][column] != 0:
        return False
    # check row:
    if value in board[row]:
        return False
    # check column:
    for r in range(9):
        if board[r][column] == value:
            return False
    # check cell:
    for r in range((row//3)*3, (row//3 + 1)*3):
        for col in range((column//3)*3, (column//3 + 1)*3):
            if board[r][col] == value:
                return False
    return True


def solve(board):
    global count
    count += 1
    found = find_empty(board)
    if not found:
        return True
    else:
        row, column = found

    for value in range(1, 10):
        if check_valid(board, value, (row, column)):
            board[row][column] = value
            if solve(board):
                return True
            board[row][column] = 0
    return False


show_board(start_board)
print("\n----------------------\n")
solve(start_board)
show_board(start_board)
print("\nSudoku solved in",count,"steps.")
