from game_scores import game_scores
import numpy as np
import matplotlib.pyplot as plt
number_of_games=1000
number_of_players=len(game_scores())


#print('above this doesnt matter')
total_games_won=np.zeros((number_of_players,1))
for gamecounter in range(number_of_games):
    #print('for game number', gamecounter )
    game_totals=game_scores()
    #print(game_totals)
    winner_of_game=np.argmax(game_totals)
    #print(winner_of_game)
    total_games_won[winner_of_game]+=1
print(total_games_won)
