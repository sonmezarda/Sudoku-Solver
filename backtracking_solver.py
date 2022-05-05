from regex import F


board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

def show_board(board):
    for row in range(9):
        for column in range(9):
            print(f"{board[row][column]}" ,end='')
            if (column+1) % 3 == 0 and column != 0:
                print('|',end='')
            else:
                print(' ',end='')
        print("")
        if (row+1) % 3 == 0 and row != 0:
            print('- - - - - - - - -')

def find_empyt(board): #finds closest empty cell
    founded = False
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                founded = row, column
                break
        if founded:
            break
    return founded   

def check_valid(board, row, column, value):
    #check empty:
    if board[row][column] != 0:
        return False
    #check row:
    if value in board[row]:
        return False
    #check column:
    for r in range(9):
        if board[r][column] == value:
            return False
    #check cell:
    for r in range((row//3)*3 , (row//3 + 1)*3):
        for col in range((column//3)*3 , (column//3 + 1)*3):
            if board[r][col] == value:
                return False
    return True
     
show_board(board)
print(check_valid(board,1,3,4))
