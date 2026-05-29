import random


def displayboard(board):
    print(f'''
    1   2   3   4   5
1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}
----------------------
2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}
----------------------
3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}
----------------------
4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}
----------------------
5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}
    ''')

def player_choice(row_or_column):
    while True:
        try:
            num = int(input(f'Enter a {row_or_column} (1 - 5): ')) - 1

            if num >= 0 and num <= 4:
                return num
            else:
                print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter an integer")



def place_bot_ships(board):
    print('The bot is now choosing spots!')
    i = 0

    while i < 4:
        row = random.randint(0, 4)
        col = random.randint(0, 4)

        if board[row][col] != 'X':
            continue
        board[row][col] = 'S'
        i += 1
    displayboard(board)


def place_player_ships(board):
    ''''''
    i = 0
    displayboard(board)

    while i < 4:
        row = player_choice('row')
        col = player_choice('column')

        if board[row][col] != 'X':
            print('Space not available')
            continue
        board[row][col] = 'S'
        displayboard(board)
        i += 1


def bot_hit(board, hiddenboard, hits):
    print('The bot is now selecting a target!')

    row = random.randint(0, 4)
    col = random.randint(0, 4)

    if hiddenboard[row][col] == 'X':
        board[row][col] = 'M'
    else:
        board[row][col] = 'H'
        hits += 1
    displayboard(board)
    return hits


def player_hit(board, hiddenboard, hits):
    row = player_choice('row')
    col = player_choice('column')

    if hiddenboard[row][col] == 'X':
        board[row][col] = 'M'
    else:
        board[row][col] = 'H'
        hits += 1
    displayboard(board)
    return hits

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
    
    place_bot_ships(hiddencomputerboard)
    place_player_ships(hiddenboard)
    player_hits = 0
    bot_hits = 0

    while True:
        bot_hits = bot_hit(board, hiddenboard, bot_hits)

        if bot_hits == 4: 
            print("The bot won!")
            break

        player_hits = player_hit(computerboard, hiddencomputerboard, player_hits)

        if player_hits == 4: 
            print("Congrats, You won!")
            break


main()


  