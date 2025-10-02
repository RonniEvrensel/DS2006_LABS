import random
print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds = 0

# lists to store rolls
list_of_player1_rolls = []
list_of_player2_rolls = []

while (player1_wins != 3 and player2_wins != 3):
    input("\nPress ENTER to roll the dice...")

    rounds += 1

    player1_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1_roll)
    list_of_player1_rolls.append(player1_roll)

    player2_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2_roll)
    list_of_player2_rolls.append(player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player1_roll < player2_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")

    if player1_wins == 3:
        print("Player 1 is unstoppable! It took", rounds, "rounds.")
        print("\nHere is the summary: ")
        for i in range(len(list_of_player1_rolls)):
            print("Round", i+1, ": Player 1 rolled", list_of_player1_rolls[i], ", Player 2 rolled", list_of_player2_rolls[i])

        Filename = input("\nEnter the filename to save the result: ")
        with open(Filename, "w") as file:
            for i in range(len(list_of_player1_rolls)):
                file.write(f"Round {i+1}: Player 1 rolled {list_of_player1_rolls[i]}, Player 2 rolled {list_of_player2_rolls[i]}\n")

    elif player2_wins == 3:
        print("Player 2 is unstoppable! It took", rounds, "rounds.")
        print("\nHere is the summary: ")
        for i in range(len(list_of_player1_rolls)):
            print("Round", i+1, ": Player 1 rolled", list_of_player1_rolls[i], ", Player 2 rolled", list_of_player2_rolls[i])

        Filename = input("\nEnter the filename to save the result: ")
        with open(Filename, "w") as file:
            for i in range(len(list_of_player1_rolls)):
                file.write(f"Round {i+1}: Player 1 rolled {list_of_player1_rolls[i]}, Player 2 rolled {list_of_player2_rolls[i]}\n")
