import random


def displayboard(board):
    print(f'''
    1   2   3   4   5
1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
----------------------
2 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
----------------------
3 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
----------------------
4 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
----------------------
5 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
    ''')


def place_bot_ships(board, numship):
    for i in range(numship):
        row = random.randint(0, 4)
        col = random.randint(0, 4)

        if board[row][col] != ' ':
            continue
        board[row][col] = 'S'
        displayboard(board)


def place_player_ships(board, numship):
    ''''''
    for i in range(numship):
        row = int(input('Enter row: ')) - 1
        col = int(input('Enter column: ')) - 1

        if board[row][col] != ' ':
            continue
        board[row][col] = 'S'
        displayboard(board)

def bot_hit(board, hiddenboard):
    row = random.randint(0, 4)
    col = random.randint(0, 4)

    if hiddenboard[row][col] == ' ':
        board[row][col] = 'M'
    else:
        board[row][col] = 'H'
    displayboard(board)

def player_hit(board, hiddenboard):
    row = int(input('Enter row: ')) - 1
    col = int(input('Enter column: ')) - 1

    if hiddenboard[row][col] == ' ':
        board[row][col] = 'M'
    else:
        board[row][col] = 'H'
    displayboard(board)

def main():
    board = [['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ]
    
    hiddenboard = [['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ]
    
    computerboard = [['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ]
    
    hiddencomputerboard = [['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ['X','X','X','X','X'],
            ]
    
    place_bot_ships(computerboard, 4)
    place_player_ships(board, 4)

    while True:
        bot_hit(board, hiddenboard)
        player_hit(computerboard, hiddencomputerboard)

main()