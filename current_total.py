#uses roller to get the current total

from roller import roll_dice
from player_A import player_A_strat
total=0
current_roll=2
number_of_players=1
player_A_in=1
all_players=[player_a_in]
while current_roll>1.1:
    while number_of_players>.1:
        current_roll=roll_dice()
        print('the current roll is')
        print(current_roll)
        if current_roll>2:
            total=total+current_roll
        elif current_roll == 2:
            if total==0:
                total=4
            else:
                total=total*2
        else:
            print('round over rolled a 1')
            total=0
            number_of_players=0
        print(total)
        player_a_in=player_A_strat(total)

        if player_a_in==0

    else:
        print('the round is over there are no players')
        break
else:
    print('the round is over a one was rolled')