# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0




# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 8)


print("Player 1 rolled: ",player1_roll)

player2_roll = random.randint(1, 8)

print("Player 2 rolled: ",player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    winner= "player 1 wins this round"
    print("Because ", player1_roll," is greater than ", player2_roll)
    winner= "player1_wins"
elif player1_roll < player2_roll:
    player2_wins += 1
    winner= "player 2 wins this round"
    print("Because ", player2_roll, "is greater than", player1_roll)

else:
    print("Amaaazzinng! This round has a tie!")

    


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is unstoppable! ")
elif player2_wins == 3:
    print("Player 2 is the king! ")
else:
    print("What a battle! Keep going guys! ")

input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 8)


print("Player 1 rolled: ",player1_roll)

player2_roll = random.randint(1, 8)

print("Player 2 rolled: ",player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    winner= "player 1 wins this round"
    print("Because ", player1_roll," is greater than ", player2_roll)
    winner= "player1_wins"
elif player1_roll < player2_roll:
    player2_wins += 1
    winner= "player 2 wins this round"
    print("Because ", player2_roll, "is greater than", player1_roll)

else:
    print("Amaaazzinng! This round has a tie!")

    


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is unstoppable! ")
elif player2_wins == 3:
    print("Player 2 is the king! ")
else:
    print("What a battle! Keep going guys! ")

input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 8)


print("Player 1 rolled: ",player1_roll)

player2_roll = random.randint(1, 8)

print("Player 2 rolled: ",player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    winner= "player 1 wins this round"
    print("Because ", player1_roll," is greater than ", player2_roll)
    winner= "player1_wins"
elif player1_roll < player2_roll:
    player2_wins += 1
    winner= "player 2 wins this round"
    print("Because ", player2_roll, "is greater than", player1_roll)

else:
    print("Amaaazzinng! This round has a tie!")

    


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is unstoppable! ")
elif player2_wins == 3:
    print("Player 2 is the king! ")
else:
    print("What a battle! Keep going guys! ")

player1_roll = random.randint(1, 8)


print("Player 1 rolled: ",player1_roll)

player2_roll = random.randint(1, 8)

print("Player 2 rolled: ",player2_roll)

if player1_roll > player2_roll:
    player1_wins += 1
    winner= "player 1 wins this round"
    print("Because ", player1_roll," is greater than ", player2_roll)
    winner= "player1_wins"
elif player1_roll < player2_roll:
    player2_wins += 1
    winner= "player 2 wins this round"
    print("Because ", player2_roll, "is greater than", player1_roll)

else:
    print("Amaaazzinng! This round has a tie!")

    


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is unstoppable! ")
elif player2_wins == 3:
    print("Player 2 is the king! ")
else:
    
    print("What a battle! Keep going guys! ")



    





