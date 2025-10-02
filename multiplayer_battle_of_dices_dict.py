import dice

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

for i in range(number_of_players):
    p = {
        "name": input(f"Name of player {i+1}: "),
        "email": input(f"Email of player {i+1}: "),
        "country": input(f"Country of player {i+1}: "),
        "wins": 0,
        "rolls": []
    }
    players.append(p)

while not gameover:
    input("Press ENTER to roll the dice...")
    current_totals = []
    for p in players:
        roll = dice.rollD6()
        p["rolls"].append(roll)
        current_totals.append(roll)
        print(f"Player {p['name']} rolled: {roll}")

    max_roll = max(current_totals)
    winners = []
    for idx, p in enumerate(players):
        if current_totals[idx] == max_roll:
            p["wins"] += 1
            winners.append(p["name"])
    print(f"Winners of this round: {winners}")

    rounds += 1

    for p in players:
        if p["wins"] >= winning_score:
            print(f"\n{p['name']} is the newest Battle of Dices champion!")
            print("It took", rounds, "rounds.")
            gameover = True
            break

if gameover:
    filename = input("Enter the filename to save the results: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Player information:\n")
        for p in players:
            file.write(f"Name: {p['name']}\n* E-mail: {p['email']}\n* Country: {p['country']}\n* Wins: {p['wins']}\n\n")
        file.write("Game rounds:\n")
        for r in range(rounds):
            rolls_str = ""
            for i, p in enumerate(players):
                rolls_str += f"({p['name']} rolled {p['rolls'][r]})"
                if i < len(players) - 1:
                    rolls_str += ", "
            file.write(f"Round {r+1}: {rolls_str}\n")
    print("Game over! Results saved successfully.")