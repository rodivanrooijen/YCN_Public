# TIC TAC TOE GAME
# the requirements for this game are:
# 1. 2 players should be able to play the game (both sitting at the same computer)
# 2. The board should be printed out every time a player makes a move
# 3. You should be able to accept input of the player position and then place a symbol on the board

#  Display the board
def display_board(board):
    print('Speelbord')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    pass

# Test the board display
begin_bord = ['#','1','2','3','4','5','6','7','8','9']
#display_board(begin_bord)

print("Welkom bij Tic Tac Toe!")

# Vraag speler 1 om X of 0 te kiezen
def speler_icoon_input():
    speler_icoon=''
    while not (speler_icoon == 'X' or speler_icoon == 'O'):
        speler_icoon = input('Speler 1: Wil je X of O zijn? ').upper()
    if speler_icoon == 'X':
        speler_icoon = ('X', 'O')
    else:
        speler_icoon = ('O', 'X')
    print('---------------------------------------------------------')
    print(f'Speler 1 begint met {speler_icoon[0]}, speler 2 begint met {speler_icoon[1]}')
    return speler_icoon
    
speler_icoon_def = speler_icoon_input()

print('Het spel begint nu, speler 1 mag beginnen')
print('---------------------------------------------------------')
display_board(begin_bord)
def speler_input_func():
    speler_input=''
    beurt=1
    if (beurt==1 or beurt==3 or beurt==5 or beurt==7 or beurt==9):
        speler_aandebeurt = '1'
    elif (beurt==2 or beurt==4 or beurt==6 or beurt==8):
        speler_aandebeurt = '2'
    print('---------------------------------------------------------')
    print(f'Speler {speler_aandebeurt} is aan de beurt, kies een nummer van 1 tot 9: ')
    while not speler_input in range(1,10):
        speler_input = int(input('Kies een nummer van 1 tot 9: '))
    else:
        beurt += 1
        print(beurt)
        print(speler_icoon_def[1])
        speler_input = int(speler_input)
        
        if speler_aandebeurt == '1':
            begin_bord[speler_input] = speler_icoon_def[0]
        elif speler_aandebeurt == '2':
            begin_bord[speler_input] = speler_icoon_def[1]
            

    return speler_input
speler_input_func()

display_board(begin_bord)

speler_input_func()

display_board(begin_bord)

speler_input_func()

display_board(begin_bord)



# 2. Ask player 1 for their move
# 3. Check if the game is won,tied, lost, or ongoing
# 4. Ask player 2 for their move
# 5. Check if the game is won,tied, lost, or ongoing
# 6. Repeat 2-5 until the game is won or tied
# 7. Ask if the players want to play again
# 8. If yes, start over at 1
# 9. If no, exit the game
# 10. Display the final score