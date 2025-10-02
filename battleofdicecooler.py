import dice

print("🎲 Welcome to dice(The COOLER Edition) 🎲")


# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds = 0

while (player1_wins != 3 and player2_wins != 3):
# Round 1
    input("\nPress ENTER to roll the dice...")

    rounds +=1

 #2 dices
    player1_roll1 = dice.rollD6()
    player1_roll2 = dice.rollD4()
    player1_total = player1_roll1 + player1_roll2


    print("Player 1 rolled:", player1_roll1, "and", player1_roll2, "(total =", player1_total, ")")

#player 2 dice

    player2_roll1 = dice.rollD6()
    player2_roll2 = dice.rollD4()
    player2_total = player2_roll1 + player2_roll2

    print("Player 2 rolled:", player2_roll1, "and", player2_roll2, "(total =", player2_total, ")")


    if player1_total > player2_total:
        player1_wins += 1
        print("PLayer 1 wins because ", player1_roll1, "+",player1_roll2, " is greater than ", player2_roll1, "+" ,player2_roll2,)
       
    elif player1_total < player2_total:
        player2_wins += 1
        print("Player 2 wins because ", player2_roll1, "+", player2_roll2, "is greater than", player1_roll1, "+",player1_roll2,)

    else: 
        print("Amaaazzinng! This round has a tie!")


    


    input("\nPress ENTER to continue...")

 # So far so good right? But how to check who got the highest roll?


 # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

 # Round check for each round u dont have to use player 2 roll because both of them will still roll
    
    if player1_roll1 and player1_roll2 and player2_roll1 and player2_roll2: 
        print("Round", rounds)

    elif player1_total == player2_total:
     print("round", rounds,)


        # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 is unstoppable! It took", rounds, "rounds.")
    elif player2_wins == 3:
        print("Player 2 is the king! It took", rounds, "rounds.")
