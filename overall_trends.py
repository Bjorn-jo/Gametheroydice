from game_scores import game_scores
import numpy as np
import matplotlib.pyplot as plt
number_of_games=10000
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
#print(total_games_won)
number_of_games_won=np.zeros(len(total_games_won))
for player in range(len(total_games_won)):
    #print(player)
    number_of_games_won[player]=(total_games_won[player][0])
print(number_of_games_won)

def create_bar_graph(data):
    #       a       b           c       d           e           f           g                       h                       i                          j 
    x=(   '50.',   '100.',   '200.',   '75.',   '800.',  '1/6 chance.',  '1/12 chance.',  'stops after round 6', 'stops after round 12.', 'lastplayerrolling.')
    #x=np.zeros(len(data))
    #x[0]=50
    #for counti in range(1,len(total_games_won)):
    #    x[counti]=x[counti-1]*2
    #print(x)
    plt.bar(x, data)
    plt.xlabel('write score when total is greater than x axis')
    plt.ylabel('number of games won')
    plt.title('odds of winning stupid dice game')
    plt.show()
create_bar_graph(number_of_games_won)