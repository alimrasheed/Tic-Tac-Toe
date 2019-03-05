#functions
def check_win(board,marker):
    if((board[0]==board[1]==board[2]==marker) or
       (board[3]==board[4]==board[5]==marker) or
       (board[6]==board[7]==board[8]==marker) or
       (board[0]==board[4]==board[8]==marker) or
       (board[2]==board[4]==board[6]==marker) or
       (board[0]==board[3]==board[6]==marker) or
       (board[1]==board[4]==board[7]==marker) or
       (board[2]==board[5]==board[8]==marker)):
        return True
        replay()
def check_Tie():
    for i in board:
        if board[i]=='-':
            return False
        else:
            return True

def player_input():
    marker=""
    while marker!='X' or marker!='O':
        marker=input('Do you want to be X or O?:').upper()
        if marker=='X':
            return ('X','O')
        else:
            return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):
    if board[position]==" ":
        return True
    else:
        return False

def game_over():
    if space_check():
        return False
    else:
        return 'Game Over!'

def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    slot_choice=int(input("Enter your next position"))
    if space_check(board,slot_choice):
        return slot_choice
    else:
        print('Oops! The slot is already occupied')

def replay():
    res=input('Do you want to play again?(Yes/No):')
    return res=='Yes'


#####GAME ########


from IPython.display import clear_output
game_still_going=True
marker=""
def display_board(board):
    clear_output()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#while loop to keep the game running
while game_still_going:

    board=[" "]*10 #set up the board
    play_game=input('Ready to play the game?(Yes/No)')
    turn=choose_first() #choose the player
    player1_marker,player2_marker=player_input()
    print(turn+'will go first')
    if play_game=='Yes':
        game_on=True
    else:
        game_on=False

    player_input() #choose markers

    #GAME PLAY
    while game_on:
        #PLAYER 1
        if turn=='Player 1':
            display_board(board)

            #Choose a position
            position=player_choice(board)
            #Place a marker
            place_marker(board,player1_marker,position)
            #check win
            if check_win(board,player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on=False
            #check tie
            else:
                if  board_full(board):
                    display_board(board)
                    print("It's a Tie!")
                    game_on=False
                else:
                    turn='Player 2'  #no win,no tie? next player's turn
        else:
        #PLAYER 2
            display_board(board)

            #Choose a position
            position=player_choice(board)
            #Place a marker
            place_marker(board,player2_marker,position)
            #check win
            if check_win(board,player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on=False
            #check tie
            else:
                if  board_full(board):
                    display_board(board)
                    print("It's a Tie!")
                    game_on=False
                else:
                    turn='Player 1'
if not replay():
    game_on=False
