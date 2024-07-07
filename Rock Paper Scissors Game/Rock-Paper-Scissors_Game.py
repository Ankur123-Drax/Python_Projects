import random

player_name = input("Enter the player name :-")
win_player = 0
win_ai = 0
tie = 0
while True:
    i = int(input(f"{player_name} choose -:\ni) 0 for Rock,\nii) 1 for Paper,\niii) 2 for Scissor\n:-"))
    choice = ["Rock", "Paper", "Scissor"]
    player_Choice = ''.join(choice[i])

    print(f"{player_name} choose :- {player_Choice}")
    a = random.randint(0, 2)
    ai_choice = ''.join(choice[a])
    print("AI choose :- ", ai_choice)
    if player_Choice == "Rock" and ai_choice == "Paper":
        print("AI win the Game")
        win_ai += 1
    elif player_Choice == "Paper" and ai_choice == "Rock":
        print(f"{player_name} win the Game")
        win_player += 1
    elif player_Choice == "Rock" and ai_choice == "Scissor":
        win_player += 1
    elif player_Choice == "Scissor" and ai_choice == "Rock":
        print("AI win the Game")
        win_ai += 1
    elif player_Choice == "Paper" and ai_choice == "Scissor":
        print("AI win the Game")
        win_ai += 1
    elif player_Choice == "Scissor" and ai_choice == "Paper":
        print(f"{player_name} win the Game")
        win_player += 1
    elif player_Choice == "Rock" and ai_choice == "Rock":
        print("The game Ties")
        tie += 1
    elif player_Choice == "Scissor" and ai_choice == "Scissor":
        print("The game Ties")
        tie += 1
    elif player_Choice == "Paper" and ai_choice == "Paper":
        print("The game Ties")
        tie += 1
    print(f"Total Tie of game{tie}.")
    print(f"Total win of {player_name}:- {win_player}")
    print(f"Total win of AI:- {win_ai}")
    ch = input("Do you want to play again:(y/n) ? :-")
    match ch:
        case "y":
            True
        case "n":
            False
            break
        case _:
            print("Invalid option selected")
            break
