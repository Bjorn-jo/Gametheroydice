import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    total_score = 0
    while True:
        roll = roll_dice()
        #print("Rolled:", roll)
        if roll == 1:
            total_score += roll
            #print("Oops! Rolled a 1. Total score:", total_score)
            break
        elif roll == 2:
            total_score *= 2
            #print("Nice! Rolled a 2. Doubled the total score to:", total_score)
        else:
            total_score += roll
            #print("Added", roll, "to the total score. New total score:", total_score)
    return total_score


number_of_plays=1000
total=0
for i in range(number_of_plays):
    total+=play_game()
mean=total/number_of_plays
print(mean)