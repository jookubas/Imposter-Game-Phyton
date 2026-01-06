import random

#Aditional

def clear():
    print("\n" * 40)

def pause():
    input("Press Enter to continue ")

#Meniu

def main_menu():
    while True:
        print(" IMPOSTER Terminal Game ")
        print("1. Start Game")
        print("2. About Game")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            start_game()
        elif choice == "2":
            about()
        elif choice == "3":
            print("Ending the game, Goodbye!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        else:
            print("Invalid choice")
            pause()

#About

def about():
    clear()
    print("   This is IMPOSTER Terminal Game   ")
    print(" In this game, players are assigned roles of either 'IMPOSTER' or 'PLAYER'")
    print(" Players with the 'PLAYER' role receive a secret word, while 'IMPOSTER' players must guess it.")
    print(" The game continues until players decide to reveal the roles and the secret word")
    print(" Enjoy playing!")
    pause()

# Players Input

def get_players():
    players = []
    print("Enter player names one by one Leave blank to finish")

    while True:
        name = input("> ")
        if name == "":
            break
        players.append(name)

    return players

#Imposter Count

def get_imposter_count(player_count):
    while True:
        try:
            count = int(input("Enter number of IMPOSTERS: "))
            if 0 < count < player_count:
                return count
            else:
                print("Enter a valid number of IMPOSTERS.")
        except:
            print("Enter a number.")

#Roles Assignment

def assign_roles(players, imposters_count):
    roles_list = ["IMPOSTER"] * imposters_count + ["PLAYER"] * (len(players) - imposters_count)
    random.shuffle(roles_list)

    roles = {}
    for i in range(len(players)):
        roles[players[i]] = roles_list[i]

    return roles

#Word

def get_word():
    words = [
        "PIZZA", "CAR", "COMPUTER",
        "SCHOOL", "CAT", "PHONE", "MOVIE",
        "RIVER", "MOUNTAIN", "GARDEN", "BOOK",
        "BICYCLE", "OCEAN", "CITY", "FOREST",
        "TRAIN", "AIRPLANE", "HOUSE", "BRIDGE",
        "GUITAR", "TELEVISION", "KITCHEN", "DESK",
        "WINDOW", "CUP", "TABLE", "CHAIR"
    ]
    return random.choice(words)

#Roles Show

def show_roles(players, roles, word):
    for i, player in enumerate(players):
        clear()
        print(f"{i+1} Player: {player}\n")
        print("ROLE:", roles[player])

        if roles[player] == "IMPOSTER":
            print("WORD: ??? (guess the word!)")
        else:
            print("WORD:", word)

        pause()

#Reveal

def reveal(players, roles, word):
    clear()
    print(" REVEAL \n")
    print(f"Real word: {word}\n")

    for p in players:
        print(f"{p}: {roles[p]}")

    pause()


#Game

def start_game():
    clear()
    players = get_players()

    if len(players) < 3:
        print("Need at least 3 players.")
        pause()
        return

    imposters_count = get_imposter_count(len(players))
    roles = assign_roles(players, imposters_count)
    word = get_word()

    show_roles(players, roles, word)

    clear()
    print("All roles have been assigned.")
    print("Now talk to find the IMPOSTERS!")
    print("Enter 'reveal' when you want to reveal the roles and the word ")

    while True:
        cmd = input("> ").lower()
        if cmd == "reveal":
            reveal(players, roles, word)
            break
        else:
            print("Unknown command. Type 'reveal' to end the game ")

#Start

main_menu()
