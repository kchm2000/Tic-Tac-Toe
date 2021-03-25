# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:09:42 2020

@author: Choo Hongming Kent
Functions used in the TTT_main2 file.
"""

# prints board, coordinates - 1 is the index value of the board
def display_board(board):
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "   1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "   4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "   7 | 8 | 9")
    print("\n")
    
    return


# validates players inputs then assigns value to empty slot
def player_input(board, player):
    
    is_valid_coordinates = False
    is_empty_coordinates = False
    
    print(player + "\'s turn")
    
    # validation integer 1 to 9 then only can input in empty "-" slots
    while not (is_valid_coordinates and is_empty_coordinates): 
    
        coordinates = input("Input coordinates 1 to 9 in empty slots: ")
        # input 1 to 9 integer?
        if coordinates in ["1","2","3","4","5","6","7","8","9"]:
    
            is_valid_coordinates = True
            # is the coordinates empty?
            if board[int(coordinates)-1] == "-":
                
                is_empty_coordinates = True
            else:
                print("Error for your input coordinates: {} has been inputted.".format(coordinates))
                
        else:
            print("Error for your input coordinates: {} not valid.".format(coordinates))
    
    # input player X or O into coordinates in board list
    board[int(coordinates)-1] = player
    
    display_board(board)
    
    return
    
# check for winner or draw otherwise continue game
def check_game_over(board):
    
    # check for winner
    winner = check_win(board)
    # check for empty slots
    is_empty = check_empty(board)
    
    # game not over if there is no winner and game not drawn
    if not winner and is_empty:
        is_game_over = False
        is_draw = False
    # check the return values for check_win and check_draw to determine draw/winner   
    elif winner == "X":
        is_game_over = True
        is_draw = False
        print("X is winner")
    elif winner == "O":
        is_game_over = True
        is_draw = False
        print("O is winner")
    elif not is_empty and not winner:
        is_game_over = True
        is_draw = True
        print("Drawn game")
    
    return is_game_over, winner, is_draw

#check for wins by having equal values vertically/horizontally/diagonally

def check_win(board):
    # horizontal win and no blank slots
    if board[0] == board[1] == board[2] and (board[0] != "-"):
        winner = board[0]
    elif board[3] == board[4] == board[5] and (board[3] != "-"):
        winner = board[3]
    elif board[6] == board[7] == board[8] and (board[6] != "-"):
        winner = board[7]
    # vertical win and no blank slots
    elif board[0] == board[3] == board[6] and (board[0] != "-"):
        winner = board[0]
    elif board[1] == board[4] == board[7] and (board[1] != "-"):
        winner = board[1]
    elif board[2] == board[5] == board[8] and (board[2] != "-"):
        winner = board[2]
    # diagonal win and no blank slots
    elif board[0] == board[4] == board[8] and (board[4] != "-"):
        winner = board[4]
    elif board[6] == board[4] == board[2] and (board[4] != "-"):
        winner = board[4]
    else:
        winner = False
        
    return winner

# check for empty slots
def check_empty(board):
    # if all coordinates are filled not empty
    if "-" not in board:
        return False
    # there are still empty slots
    elif "-" in board:   
        return True

# flip player from X to O or O to X
def flip_player(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player   

# asks the user whether they want to continue yes or no
def want_to_continue():
    
    is_input_valid = False
    
    while not is_input_valid:
        #ask for input of yes/no        
        ask_to_continue = input("Do you want to start again? Type only yes/no: ")
        
        #if equal yes continue game true
        if ask_to_continue == "yes" or ask_to_continue == "Yes"  :
            is_continue = True
            is_input_valid = True
        #if equal no continue game false
        elif ask_to_continue == "no" or ask_to_continue == "No":
            is_continue = False
            is_input_valid = True
        # error message if not yes or no
        else:
            print("Error in your input: {}. Type only yes/no".format(ask_to_continue))
            is_input_valid = False
            
    return is_continue

#asks for how many games you want to play
def best_of_num_games():
    
    is_valid_set = False
    # loop and keep asking for number of games you want to play
    while not is_valid_set:
        # asks for input of odd number
        ask_best_of_num = input("Best of how many games? Input 1 to 9 please: ")
        # checks if str input is numeric else error msg
        if ask_best_of_num in ["1","2","3","4","5","6","7","8","9"]:
            is_valid_set = True
            best_of_num = int(ask_best_of_num)
        else:
            print("Error in your input: {}. Type only 1 to 9".format(ask_best_of_num))    
            
    return best_of_num
