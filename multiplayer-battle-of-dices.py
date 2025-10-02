import random

winning_score = 3
rounds = 0
gameover = False

number_of_players = int(input("How many players? "))

player_names = []
player_wins = []
player_rolls_history = []

for i in range(number_of_players):
    name = input(f"Name of player {i+1}: ")
    player_names.append(name)
    player_wins.append(0)
    player_rolls_history.append([])

while not gameover:
    input("Press ENTER to roll the dice...")
    current_rolls = []
    for i in range(number_of_players):
        roll = random.randint(1, 6)
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")

    max_roll = max(current_rolls)
    winners = []
    for i in range(number_of_players):
        if current_rolls[i] == max_roll:
            player_wins[i] += 1
            winners.append(player_names[i])
    print(f"Winners of this round: {winners}")

    rounds += 1

    for i in range(number_of_players):
        if player_wins[i] >= winning_score:
            print(f"\n{player_names[i]} is the newest Battle of Dices champion!")
            print("It took", rounds, "rounds.")
            gameover = True
            break

if gameover:
    filename = input("Enter the filename to save the results: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Game rounds:\n")
        for r in range(rounds):
            rolls_str = ""
            for i in range(number_of_players):
                rolls_str += f"({player_names[i]} rolled {player_rolls_history[i][r]})"
                if i < number_of_players - 1:
                    rolls_str += ", "
            file.write(f"Round {r+1}: {rolls_str}\n")
    print("Game over! Results saved successfully.")