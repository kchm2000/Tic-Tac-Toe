# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:37:44 2020

@author: Choo Hongming Kent

starts with a random player, then asks how many games you want to play.
game loop continues until number of rounds is completed. Then asks player whether they want to
play more rounds. On every new match program will always alternate the player that starts.
The program also keeps track of the total score in a set. All inputs are validated.
"""

from random import randint
   
# randomize the starting player

random_start = randint(1,2) 
# if random number is 1, player X starts
if random_start == 1:
    player_start = "X"
# if random number is 2, player O starts
elif random_start == 2:
    player_start = "O"
#import all necessary functions from TTT_Functions
from TTT_Functions import display_board, player_input, check_game_over, flip_player, want_to_continue, \
                          best_of_num_games

#initialize loop for whether you want to continue a new set of games
is_continue = True
#loop for whether you want to continue a new set of games
while is_continue:
    #set of how many games, best of series
    best_of_num = best_of_num_games()
    #initialize win and draw count for each player
    O_win = 0
    X_win = 0
    draw_count = 0
    #initialize game count 
    game = 1
    #loop until game is equal to number of games you inputted
    while game <= best_of_num:
        print("-----------------------------------------------")
        print("Round: ", game)
        # empty board
        board = ["-","-","-",\
                 "-","-","-",\
                 "-","-","-",]
        #display empty board
        display_board(board)
        
        # intialize game not over to start loop until game is over
        is_game_over = False
        
        # intialize player that will be starting
        player = player_start
        
        # while game is still going continue this loop
        while not is_game_over: 
            # input coordinates
            player_input(board,player)
            
            # check game over if someone wins or there is a draw
            is_game_over, winner, is_draw = check_game_over(board)
            
            # after turn switch player
            player = flip_player(player)
        
        # after each round change starting player    
        player_start = flip_player(player_start)
        # if else statements to add to win and draw counts
        if winner == "X":
            X_win += 1
        elif winner == "O":
            O_win += 1
        elif not winner and is_draw:
            draw_count += 1
        
        print("Score is O:{}, X:{}, Draw:{}".format(O_win, X_win, draw_count))
        # immediately end if win more than half the games in given set
        # if number of games are odd
        if best_of_num%2 != 0:
            if O_win == ((best_of_num + 1)/2):
                break
            elif X_win == ((best_of_num + 1)/2):
                break
        # if number of games are even
        if best_of_num%2 == 0:
            if O_win == (best_of_num/2 + 1):
                break
            elif X_win == (best_of_num/2 + 1):
                break
            
        game += 1
    #check for ultimate winner and if series is drawn
    if X_win > O_win:
        print("X is grand winner ")
    elif O_win > X_win:
        print("O is grand winner ")
    elif (draw_count == best_of_num) or (X_win == O_win):
        print("The series is drawn ")
    #want to continue another set?
    is_continue = want_to_continue()
    