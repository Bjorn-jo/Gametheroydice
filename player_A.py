import random
def player_A_strat(total):
    if total>50:
        #means player a scores for that round
        return(0)
    else:
        #means player A is still going
        return(1)
def player_B_strat(total):
    if total>100:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_C_strat(total):
    if total>200:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_D_strat(total):
    if total>75:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_E_strat(total):
    if total>800:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_F_strat(total):
    total=random.randint(0,6)
    if total==6:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_G_strat(total):
    total=random.randint(0,12)
    if total==12:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_H_strat(round):
    if round>6:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_I_strat(round):
    if round>12:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
def player_J_strat(number_of_players_in):
    if number_of_players_in==1:
        #means player scores for that round
        return(0)
    else:
        #means player is still going
        return(1)
