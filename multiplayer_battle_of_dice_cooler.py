import dice

print("🎲 Welcome to dice(The COOLER Edition) 🎲")

winning_score = 3
rounds = 0
gameover = False

player_names = []
player_wins = []

number_of_players = int(input("How many players? "))

for i in range(number_of_players):
    name = input(f"whats the name of Player {i+1}? ")
    player_names.append(name)

for i in range(number_of_players):
    player_wins.append(0)

player_rolls_history = []
for i in range(number_of_players):
    player_rolls_history.append([])

while gameover is False: 
    input("\nPress ENTER to roll the dice...")
    print(f"Round {rounds+1}:")
    current_rolls = []

    for i in range(number_of_players):
        player_roll1 = dice.rollD6()
        player_roll2 = dice.rollD4()
        player_total = player_roll1 + player_roll2
        current_rolls.append(player_total)
        player_rolls_history[i].append(player_total)
        print("player", player_names[i], "rolled:", player_roll1, "and", player_roll2, "(total =", player_total, ")")

    max_roll = max(current_rolls)
    winners = []

    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] = player_wins[j] + 1
        
    print(f"The Winners of this round are: {winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n {player_names[z]} is the newest Battle of Dice Champion")
            print("It took", rounds+1, "rounds.")
            gameover = True

    if gameover is False:
        print("This heated battle is still going on! Who will win in the end?")
        
    rounds = rounds + 1

filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: 
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += (f"({player_names[i]} rolled {player_rolls_history[i][round_number]})")
            if i < number_of_players - 1: 
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")
