#uses roller to get the current total

from roller import roll_dice
from player_A import player_A_strat
from player_A import player_B_strat
from player_A import player_C_strat
from player_A import player_D_strat
from player_A import player_E_strat
from player_A import player_F_strat
from player_A import player_G_strat
from player_A import player_H_strat
from player_A import player_I_strat
from player_A import player_J_strat


import numpy as np
def round_scores():
    total=0
    current_roll=2
    player_A_in=1
    player_B_in=1
    player_C_in=1
    player_D_in=1
    player_E_in=1
    player_F_in=1
    player_G_in=1
    player_H_in=1
    player_I_in=1
    player_J_in=1
    all_players=[player_A_in,player_B_in,player_C_in,player_D_in,player_E_in,player_F_in,player_G_in,player_H_in,player_I_in,player_J_in]
    all_players_round_score=np.zeros((len(all_players),1))
    round=0
    while sum(all_players)>.1:
        #decideds to roll dice or will end round
        current_roll=roll_dice()
        round+=1
        #print('the current roll is')
        #print(current_roll)
        #rolls one dice form 1 to 6
        if current_roll>2:
            #adds current roll to total if it rolls 3 through 6
            total=total+current_roll
        elif current_roll == 2:
            # doubles total if it rolls a 2
            if total==0:
                total=4
            else:
                total=total*2
                
        else:
            # ends round if a 1 is rolled
            #print('round over rolled a 1')
            total=0
                        
            for i in range(len(all_players)):
                #scores 0 for all players who havent scored yet for the round
                if all_players[i]==1:
                    all_players_round_score[i]=0
                    all_players[i]=0
            #print(all_players)
            break

        #print(total)
        # checks for scoring
        if player_A_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_A_in=player_A_strat(total)
            if player_A_in == 0:
                all_players_round_score[0]=total
                #print('player a has scored')
        if player_B_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_B_in=player_B_strat(total)
            if player_B_in == 0:
                all_players_round_score[1]=total
                #print('player a has scored')
        if player_C_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_C_in=player_C_strat(total)
            if player_C_in == 0:
                all_players_round_score[2]=total
                #print('player a has scored')
        if player_D_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_D_in=player_D_strat(total)
            if player_D_in == 0:
                all_players_round_score[3]=total
                #print('player a has scored')
        if player_E_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_E_in=player_E_strat(total)
            if player_E_in == 0:
                all_players_round_score[4]=total
                #print('player a has scored')
        if player_F_in ==1:
            player_F_in=player_F_strat(total)
            if player_F_in == 0:
                all_players_round_score[5]=total
                #print('player a has scored')
        if player_G_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_G_in=player_G_strat(total)
            if player_G_in == 0:
                all_players_round_score[6]=total
                #print('player a has scored')
        if player_H_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_H_in=player_H_strat(round)
            if player_H_in == 0:
                all_players_round_score[7]=total
                #print('player a has scored')
        if player_I_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_I_in=player_I_strat(round)
            if player_I_in == 0:
                all_players_round_score[8]=total
                #print('player a has scored')
        if player_J_in ==1:
            #if current player is still in checks to see if they are still in after roll
            player_J_in=player_J_strat(sum(all_players))
            if player_J_in == 0:
                all_players_round_score[9]=total
                #print('player a has scored')

        #update number of players
        all_players=[player_A_in,player_B_in,player_C_in,player_D_in,player_E_in,player_F_in,player_G_in,player_H_in,player_I_in,player_J_in]
        

    #print('the round is over')


    #print(all_players_round_score)
    return(all_players_round_score)
#round_scores()