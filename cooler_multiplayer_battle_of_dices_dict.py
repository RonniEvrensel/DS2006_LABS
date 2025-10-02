import copy
import dice

print("🎲 Welcome to dice (The COOLER Edition) 🎲")

winning_score = 3
rounds = 0
gameover = False

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []  
}

players = []

number_of_players = int(input("How many players? "))

# info_player
for i in range(number_of_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"What is the name of player {i+1}? ")
    player["email"] = input(f"What is the email of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")
    players.append(player)

# loop
while not gameover:
    input("\nPress ENTER to roll the dice...")
    print(f"Round {rounds + 1}:")
    current_totals = []

    # player_rolls
    for player in players:
        roll1 = dice.rollD6()
        roll2 = dice.rollD4()
        total = roll1 + roll2
        player["rolls"].append(total)
        current_totals.append(total)
        print("player", player["name"], "rolled:", roll1, "and", roll2, "(total =", total, ")")

    # WHo wins
    max_roll = max(current_totals)
    winners = []
    for player in players:
        if player["rolls"][-1] == max_roll:
            player["wins"] += 1
            winners.append(player["name"])

    print(f"The Winners of this round are: {winners}")

    # machwinner
    for player in players:
        if player["wins"] >= winning_score:
            print(f"\n{player['name']} is the newest Battle of Dice Champion")
            print("It took", rounds + 1, "rounds.")
            gameover = True
            break

    if not gameover:
        print("This heated battle is still going on! Who will win in the end?")

    rounds += 1

# saving to file
filename = input("\nEnter the filename to save the results: ").strip()
with open(filename, "w", encoding="utf-8") as file:
    file.write("Player information:\n")
    for player in players:
        file.write(
            f"Name: {player['name']}\n"
            f"* E-mail: {player['email']}\n"
            f"* Country: {player['country']}\n"
            f"* Wins: {player['wins']}\n\n"
        )

    file.write("Game rounds:\n")
    for r in range(rounds):
        rolls_str = ""
        for i, player in enumerate(players):
            rolls_str += f"({player['name']} rolled {player['rolls'][r]})"
            if i < len(players) - 1:
                rolls_str += ", "
        file.write(f"Round {r + 1}: {rolls_str}\n")

print("\nGame over! Results saved successfully.")
