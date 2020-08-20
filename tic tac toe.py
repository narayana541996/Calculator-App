from time import sleep
#from IPython.display import clear_output

positions = list(range(1,10))

def board(positions):
    #positions = list(range(0,10))
    #clear_output()
    print(positions[0],'|',positions[1],'|',positions[2])
    print('-'*10)
    print(positions[3],'|',positions[4],'|',positions[5])
    print('-'*10)
    print(positions[6],'|',positions[7],'|',positions[8])
    return positions

def win_check(board,mark):
    return( (board[0] == board[1] == board[2] == mark)or
            (board[3] == board[4] == board[5] == mark)or
            (board[6] == board[7] == board[8] == mark)or
            (board[0] == board[3] == board[6] == mark)or
            (board[1] == board[4] == board[7] == mark)or
            (board[2] == board[5] == board[8] == mark)or
            (board[6] == board[4] == board[2] == mark)or
            (board[8] == board[4] == board[0] == mark))

def game_check(board):
    for step in board:
        if type(step) == int:
            game_on = True
            return game_on
        else:
            game_on = False
    return game_on
        
def game(player_1,player_2):
    game_on = True
    step = 0
    x_win = 0
    o_win = 0
    p1_steps = []
    p2_steps = []
    print('Let the game begin!')
    newboard = board(positions)
    
    while game_on == True:
        
        #if type(newboard[step]) == int:
        if step%2 == 0:
            print('player_1\'s turn,')
            position = int(input('enter the positon(between 1 to 9) you wish to take, player_1:'))
            
            if position not in p1_steps and position not in p2_steps:
                
                if position in range(1,10):
                    
                    p1_steps.append(position)
                    newboard[newboard.index(position)] = player_1
                    board(newboard)
                    #print('p1_steps:',p1_steps,'p2_steps:',p2_steps)
                    game_on = game_check(newboard)
                    win = win_check(newboard,player_1)

                    if win == True:
                        print('Player_1 win!')
                        sleep(2)
                        break
                    step += 1
                    
                else:
                    print('Sorry, invalid position, check the positions(numbers displayed on the board) available and enter a position between 1 to 10')
                    #step -= 1
                    
            else:
                print('Sorry, the position is already taken, check the positions available and choose a different one between 1 to 9')
                #step -= 1
            continue
        
        else:
            print('player_2\'s turn,')
            position = int(input('enter the positon(between 1 to 9) you wish to take, player_2:'))
            
            if position not in p1_steps and position not in p2_steps:
                if position in range(1,10):
                    p2_steps.append(position)
                    newboard[newboard.index(position)] = player_2
                    board(newboard)
                    #print('p1_steps:',p1_steps,'p2_steps:',p2_steps)                    
                    game_on = game_check(newboard)
                    win = win_check(newboard,player_2)

                    if win == True:
                        print('Player_2 win!')
                        sleep(2)
                        break
                    step += 1
                else:
                    print('Sorry, invalid position, check the positions(numbers displayed on the board) avaialable and enter a position between 1 to 10')
                    #step -= 1

            else:
                print('Sorry, the position is already taken, check the positions available and choose a different one between 1 to 9')
                #step -= 1
    play_again = input('Wish to play another game?- Type Y for yes and any other character for no ').lower()
    return play_again
    



                    
#def player_choice():
player_1 = input('Hey player_1, do you wish to be x or o? choose one ').lower()

while player_1 != 'x' and player_1 != 'o':
    print('Choose either x or o ')
    player_1 = input('x or o? ').lower()
    
if player_1 == 'x':
    print('player 1 takes x!')
    sleep(2)
    print('player_2 gets o!')
    player_2 = 'o'
    sleep(2)
    
else:
    player_2 = 'x'
    print('player_1 takes o!')
    sleep(2)
    print('player_2 gets x!')
    sleep(2)
        #return player_1,player_2
    
#players = {'player_1':player_1,'player_2':player_2}
#newboard = board(positions)

play_again = 'y'

while play_again == 'y':
    play_again = game(player_1,player_2)
    
if play_again != 'y':
    print('Bye! Hope you enjoyed the game!')
    #sleep(5)
    #exit()


    
    
    
