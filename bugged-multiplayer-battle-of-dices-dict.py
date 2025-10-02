import copy
import dice

rounds = 0

gameover = False

winning_score = 3

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

players = []

number_of_players = int(input("How many players?"))

for i in range(number_of_players):

    player = player_info.copy()

    player["name"] = input(f"What is the name of player {i+1}?")
    player["email"] = input(f"What is the email of Player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")

    players.append(player)



while gameover is False:

    print(f"Round {rounds+1}:")

    current_rolls = []

    for each_player in players:
        roll = dice.rollD6()

        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"Player {each_player['name']} rolled: {roll}")

    max_roll = max(current_rolls)

    winners = []

    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"Player  {each_player['name']} won in round {rounds}")

            winners.append(each_player['name'])
    print(f"Winners of this round: {winners}")

    for each_player in players:
        if(each_player["wins"] >= winning_score):
            print(f"\n {each_player['name']} is the newest battle of dices champion!")
            gameover = True
        
    if gameover is False:
        print("This heated battle of dices is still going on! Who will win in the end? ")

    rounds += 1



filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    file.write("Player information:\n")

    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n\n"
        )

    file.write("\nGame rounds:\n")

    for r in range(rounds):
                
        rolls_str = ""
                    
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            if i < len(players) - 1:
               rolls_str += ", "

        file.write(f"Round {r+1}:\n {rolls_str}\n")

    print("\nGame over! Results saved successfully.")


