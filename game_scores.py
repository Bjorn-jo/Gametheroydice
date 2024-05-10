from round_scores1 import round_scores
import numpy as np
#test_round=round_scores()
def game_scores():
    number_of_players=len(round_scores())
    total_score=np.zeros((number_of_players,1))
    for round in range(30):
        current_round_score=round_scores()
        #print("for round number", round, "the scores were", current_round_score)
        for player in range(number_of_players):
            total_score[player]=total_score[player]+current_round_score[player]
    #print("the total scores were",total_score)
    #winner=np.argmax(total_score)
    #print("the winner is player", winner+1)
    #if winner==0:
    #    print('the winning strat was taking anything over 20')
    #elif winner==1:
    #    print('the winning strat was taking anything over 50')
    #elif winner==2:
    #    print('the winning strat was taking anything over 100')
    return(total_score)
#game_scores()
