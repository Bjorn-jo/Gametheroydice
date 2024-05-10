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
#print(total_games_won)
number_of_games_won=np.zeros(5)
for player in range(len(total_games_won)):
    #print(player)
    number_of_games_won[player]=(total_games_won[player][0])
print(number_of_games_won)

def create_bar_graph(data):
    #x = range(len(data))
    x = ('50','100','500','1000','5000')
    plt.bar(x, data)
    plt.xlabel('score when total is greater than')
    plt.ylabel('number of games won')
    plt.title('Bar Graph')
    plt.show()
create_bar_graph(number_of_games_won)