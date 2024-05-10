#uses roller to get the current total

from roller import roll_dice
from player_A import player_A_strat
from player_B import player_B_strat
from player_C import player_C_strat
import numpy as np
def round_scores():
    total=0
    current_roll=2
    player_A_in=1
    player_B_in=1
    player_C_in=1
    all_players=[player_A_in,player_B_in,player_C_in]
    all_players_round_score=np.zeros((len(all_players),1))

    while sum(all_players)>.1:
        #decideds to roll dice or will end round
        current_roll=roll_dice()
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
        #update number of players
        all_players=[player_A_in,player_B_in,player_C_in]
        

    #print('the round is over')


    #print(all_players_round_score)
    return(all_players_round_score)
#round_scores()