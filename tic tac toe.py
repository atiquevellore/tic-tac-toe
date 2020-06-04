import random
board={'7':'','8':'','9':'','4':'','5':'','6':'','1':'','2':'','3':''}
def display():
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print(board['1']+'|'+board['2']+'|'+board['3'])
def win_check(board):
    if(board['7'] == board['8'] == board['9']):
        print('yes u won the game ')
    elif(board['4'] ==board['5'] ==board['6']):
        print('yes u won the game ') # across the middle
    elif(board['1'] ==board['2'] ==board['3']):
        print('yes u won the game ') # across the bottom
    elif(board['7'] ==board['4'] == board['1'] ):
        print('yes u won the game ') # down the middle
    elif(board['8'] ==board['5'] ==  board['2'] ):
        print('yes u won the game ') # down the middle
    elif(board['9'] ==board['6'] == board['3']):
        print('yes u won the game ')# down the right side
    elif(board['7'] ==board['5'] == board['3']):
        print('yes u won the game ') # diagonal
    elif(board['9'] ==board['5'] == board['1']):
        print('yes u won the game ')# diagonal
    else:
        print('no  u lost the game ')
c=['X','O']
turn=random.choice(c)
print('welcome to tic tac toe game')
for i in range(9):
    print('Turn for ' + turn + '. Move on which space?')
    move=input()
    board[move]=turn
    display()
    if turn == 'X':
         turn = 'O'
    else:
        turn = 'X'
win_check(board)
