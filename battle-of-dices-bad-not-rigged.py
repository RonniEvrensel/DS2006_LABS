import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables
player1_wins = 0
player2_wins = 0

# -------------------- Round 1 --------------------
input("Press ENTER to roll the dice...")

player1__round1_roll = random.randint(1, 8)
print("Player 1 rolled:", player1__round1_roll)

player2__round1_roll = random.randint(1, 8)
print("Player 2 rolled:", player2__round1_roll)

if player1__round1_roll > player2__round1_roll:
    player1_wins += 1
    print("Player 1 wins this round because", player1__round1_roll, "is greater than", player2__round1_roll)
elif player1__round1_roll < player2__round1_roll:
    player2_wins += 1
    print("Player 2 wins this round because", player2__round1_roll, "is greater than", player1__round1_roll)
else:
    print("Amaaazzinng! This round has a tie!")


print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
if player1_wins == 3:
    print("player 1 won")
    print("Here are the results!")
    print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
elif player2_wins == 3:
    print("Player 2 won!")
    print("Here are the results!")
    print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
else:
    print("What a battle! Keep going guys!")

# -------------------- Round 2 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round2_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round2_roll)

    player2__round2_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round2_roll)

    if player1__round2_roll > player2__round2_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round2_roll, "is greater than", player2__round2_roll)
    elif player1__round2_roll < player2__round2_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round2_roll, "is greater than", player1__round2_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
        print("Round 2: Player1=", player1__round2_roll, "vs Player2=", player2__round2_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
        print("Round 2: Player2=", player2__round2_roll, "vs Player1=", player1__round2_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 3 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round3_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round3_roll)

    player2__round3_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round3_roll)

    if player1__round3_roll > player2__round3_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round3_roll, "is greater than", player2__round3_roll)
    elif player1__round3_roll < player2__round3_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round3_roll, "is greater than", player1__round3_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
        print("Round 2: Player1=", player1__round2_roll, "vs Player2=", player2__round2_roll,)
        print("Round 3: Player1=", player1__round3_roll, "vs Player2=", player2__round3_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
        print("Round 2: Player2=", player2__round2_roll, "vs Player1=", player1__round2_roll,)
        print("Round 3: Player2=", player2__round3_roll, "vs Player1=", player1__round3_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 4 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round4_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round4_roll)

    player2__round4_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round4_roll)

    if player1__round4_roll > player2__round4_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round4_roll, "is greater than", player2__round4_roll)
    elif player1__round4_roll < player2__round4_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round4_roll, "is greater than", player1__round4_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
        print("Round 2: Player1=", player1__round2_roll, "vs Player2=", player2__round2_roll,)
        print("Round 3: Player1=", player1__round3_roll, "vs Player2=", player2__round3_roll,)
        print("Round 4: Player1=", player1__round4_roll, "vs Player2=", player2__round4_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
        print("Round 2: Player2=", player2__round2_roll, "vs Player1=", player1__round2_roll,)
        print("Round 3: Player2=", player2__round3_roll, "vs Player1=", player1__round3_roll,)
        print("Round 4: Player2=", player2__round4_roll, "vs Player1=", player1__round4_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 5 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round5_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round5_roll)

    player2__round5_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round5_roll)

    if player1__round5_roll > player2__round5_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round5_roll, "is greater than", player2__round5_roll)
    elif player1__round5_roll < player2__round5_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round5_roll, "is greater than", player1__round5_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
        print("Round 2: Player1=", player1__round2_roll, "vs Player2=", player2__round2_roll,)
        print("Round 3: Player1=", player1__round3_roll, "vs Player2=", player2__round3_roll,)
        print("Round 4: Player1=", player1__round4_roll, "vs Player2=", player2__round4_roll,)
        print("Round 5: Player1=", player1__round5_roll, "vs Player2=", player2__round5_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
        print("Round 2: Player2=", player2__round2_roll, "vs Player1=", player1__round2_roll,)
        print("Round 3: Player2=", player2__round3_roll, "vs Player1=", player1__round3_roll,)
        print("Round 4: Player2=", player2__round4_roll, "vs Player1=", player1__round4_roll,)
        print("Round 5: Player2=", player2__round5_roll, "vs Player1=", player1__round5_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 6 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round6_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round6_roll)

    player2__round6_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round6_roll)

    if player1__round6_roll > player2__round6_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round6_roll, "is greater than", player2__round6_roll)
    elif player1__round6_roll < player2__round6_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round6_roll, "is greater than", player1__round6_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 1: Player1=", player1__round1_roll, "vs Player2=", player2__round1_roll,)
        print("Round 2: Player1=", player1__round2_roll, "vs Player2=", player2__round2_roll,)
        print("Round 3: Player1=", player1__round3_roll, "vs Player2=", player2__round3_roll,)
        print("Round 4: Player1=", player1__round4_roll, "vs Player2=", player2__round4_roll,)
        print("Round 5: Player1=", player1__round5_roll, "vs Player2=", player2__round5_roll,)
        print("Round 6: Player1=", player1__round6_roll, "vs Player2=", player2__round6_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 1: Player2=", player2__round1_roll, "vs Player1=", player1__round1_roll,)
        print("Round 2: Player2=", player2__round2_roll, "vs Player1=", player1__round2_roll,)
        print("Round 3: Player2=", player2__round3_roll, "vs Player1=", player1__round3_roll,)
        print("Round 4: Player2=", player2__round4_roll, "vs Player1=", player1__round4_roll,)
        print("Round 5: Player2=", player2__round5_roll, "vs Player1=", player1__round5_roll,)
        print("Round 6: Player2=", player2__round6_roll, "vs Player1=", player1__round6_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 7 --------------------
# -------------------- Round 7 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    player1__round7_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round7_roll)

    player2__round7_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round7_roll)

    if player1__round7_roll > player2__round7_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round7_roll, "is greater than", player2__round7_roll)
    elif player1__round7_roll < player2__round7_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round7_roll, "is greater than", player1__round7_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 7: Player1=", player1__round7_roll, "vs Player2=", player2__round7_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 7: Player2=", player2__round7_roll, "vs Player1=", player1__round7_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 8 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round8_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round8_roll)

    player2__round8_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round8_roll)

    if player1__round8_roll > player2__round8_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round8_roll, "is greater than", player2__round8_roll)
    elif player1__round8_roll < player2__round8_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round8_roll, "is greater than", player1__round8_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 8: Player1=", player1__round8_roll, "vs Player2=", player2__round8_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 8: Player2=", player2__round8_roll, "vs Player1=", player1__round8_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 9 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round9_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round9_roll)

    player2__round9_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round9_roll)

    if player1__round9_roll > player2__round9_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round9_roll, "is greater than", player2__round9_roll)
    elif player1__round9_roll < player2__round9_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round9_roll, "is greater than", player1__round9_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 9: Player1=", player1__round9_roll, "vs Player2=", player2__round9_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 9: Player2=", player2__round9_roll, "vs Player1=", player1__round9_roll,)
    else:
        print("What a battle! Keep going guys!")

# -------------------- Round 10 --------------------
if player1_wins < 3 and player2_wins < 3:
    input("Press ENTER to roll the dice...")

    player1__round10_roll = random.randint(1, 8)
    print("Player 1 rolled:", player1__round10_roll)

    player2__round10_roll = random.randint(1, 8)
    print("Player 2 rolled:", player2__round10_roll)

    if player1__round10_roll > player2__round10_roll:
        player1_wins += 1
        print("Player 1 wins this round because", player1__round10_roll, "is greater than", player2__round10_roll)
    elif player1__round10_roll < player2__round10_roll:
        player2_wins += 1
        print("Player 2 wins this round because", player2__round10_roll, "is greater than", player1__round10_roll)
    else:
        print("Amaaazzinng! This round has a tie!")

    print("The game score is Player1", player1_wins, "vs.", player2_wins, "Player 2.")
    if player1_wins == 3:
        print("player 1 won")
        print("Here are the results!")
        print("Round 10: Player1=", player1__round10_roll, "vs Player2=", player2__round10_roll,)
    elif player2_wins == 3:
        print("Player 2 won!")
        print("Here are the results!")
        print("Round 10: Player2=", player2__round10_roll, "vs Player1=", player1__round10_roll,)
    else:
        print("What a battle! Keep going guys!")
