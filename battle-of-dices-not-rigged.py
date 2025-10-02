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
rounds = 0

#Using len for the first time
list_of_player1_rolls = []

 #list for p2

list_of_player2_rolls = []

while (player1_wins != 3 and player2_wins != 3):
# Round 
    input("\nPress ENTER to roll the dice...")

    rounds +=1

    player1_roll = random.randint(1, 8)


    print("Player 1 rolled: ",player1_roll)

    list_of_player1_rolls.append(player1_roll)
    player2_roll = random.randint(1, 8)

    print("Player 2 rolled: ",player2_roll)
    list_of_player2_rolls.append(player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
       
    elif player1_roll < player2_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll, "is greater than", player1_roll)

    else:
        print("Amaaazzinng! This round has a tie!")

    


    input("\nPress ENTER to continue...")

 # So far so good right? But how to check who got the highest roll?


 # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

 # Now we need to check if either player won.

    if player1_wins == 3:
        print("Player 1 is unstoppable! It took ", rounds,  " rounds.")


        Filename = input("Enter the filename to see the result:")
        with open(Filename, "w") as file: #w = write 
            for i in range(len(list_of_player1_rolls)):
                file.write(f"Round {i+1}: Player 1 rolled {list_of_player1_rolls[i]}, Player 2 rolled {list_of_player2_rolls[i]}\n")
        

        

        
    
    elif player2_wins == 3:
        print("Player 2 is unstoppable! It took ", rounds,  " rounds.")
        Filename = input("Enter the filename to see the result:")
        with open(Filename, "w") as file: #w = write 
            for i in range(len(list_of_player1_rolls)):
                file.write(f"Round {i+1}: Player 1 rolled {list_of_player1_rolls[i]}, Player 2 rolled {list_of_player2_rolls[i]}\n")

        

        
    