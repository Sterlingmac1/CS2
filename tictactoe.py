def print_board(board):
      print(f"{board[0][0]} |{board[0][1]} | {board[0][2]} ")
      print('----------')
      print(f"{board[1][0]} |{board[1][1]} | {board[1][2]} ")
      print('----------')
      print(f"{board[2][0]}|{board[2][1]} | {board[2][2]} ") 
def get_player_move(board, player):
      row = int(input('Enter the row you want to go: '))
      colum = int(input('Enter the colum you want to go: '))
      board[row-1][colum-1] = player
def check_winner_board(board):
            #REPLACE 'x' W PLAYER 
            if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[0][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
            elif board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                  print('o has won the game')
                  return True
            elif board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board[2][2] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            elif board[0][0] == 'x' and board [1][0] == 'x' and board [2][0] == 'x':
                  print('x has won the game')
                  return True
            elif board[0][0] == 'o' and board [1][0] == 'o' and board [2][0] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][1] == 'x' and board [1][1] == 'x' and board [2][1] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][1] == 'o' and board [1][1] == 'o' and board [2][1] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'x':
                  print('o has won the game')
                  return True
            elif board [0][0] == 'x' and board [1][1] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][0] == 'o' and board [1][1] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            elif board [2][0] == 'x' and board [1][1] == 'x' and board [0][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [2][0] == 'o' and board [1][1] == 'o' and board [0][2] == 'o':
                  print('o has won the game')
                  return True
            elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                  print('x has won the game')
                  return True
            elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'o':
                  print('o has won the game')
                  return True
            else:
                  return False
    

def check_tie(board):

    if board[0][0] == ' ' or board[0][1] == ' '  or board[0][2] == ' ' or board[1][0] == ' ' or board[1][1] == ' ' or board[1][2] == ' ' or board[2][0] == ' ' or board[2][1] == ' ' or board[2][2] == ' ':
        return False
    else: 
        print('Game is a tie!')
        exit()



def main():
      board = [[' ',' ',' '],
               [' ',' ',' '],
               [' ',' ',' ']]

      print_board(board)

      while True:    
            p1_x_or_o = input("Do you want to be x or o?")

            if p1_x_or_o == 'x':
                  p2_x_or_o = 'o'

            else:
                  p2_x_or_o = 'x'
            print_board(board)
            while True: 

                  get_player_move(board, p1_x_or_o)
                  print_board(board)
                  if check_winner_board(board) == True or check_tie(board) == True:
                        break
                  get_player_move(board, p2_x_or_o)
                  print_board(board)
                  if check_winner_board(board) == True or check_tie(board) == True:
                        break
            Play_again = input("Play again yes or no")
            if Play_again == "no":
                        break 

main()