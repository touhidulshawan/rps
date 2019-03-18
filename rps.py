# rock beats scissor
# paper beats rock
# scissor beats paper
from random import randint
# x = True
while True:
    print("\n----------------------------------\n----------------------------------")
    print("1.Rock\n2.Paper\n3.Scissor")
    player_choice = input("Choose 1 option: ")
    print("----------------------------------\n")
    player_choice = player_choice.lower()

    # computer choice
    com_choice = randint(1, 3)
    com = ""
    if com_choice == 1:
        com = "rock"
    elif com_choice == 2:
        com = "paper"
    else:
        com = "scissor"

    print(f"You choose: {player_choice}")
    print(f"Computer choice: {com}")
    print("----------------------------------\n")

    # Game Logic
    if player_choice == com:
        print("It`s Tie")
    if player_choice == "rock":
        if com == "scissor":
            print("You win !!")
        elif com == "paper":
            print("Sorry Computer wins !!")
    elif player_choice == "paper":
        if com == "rock":
            print("You win !!")
        elif com == "scissor":
            print("Sorry Computer wins !!")
    elif player_choice == "scissor":
        if com == "paper":
            print("You win !!")
        elif com == "rock":
            print("Sorry Computer wins !!")
    else:
        print("Sorry Computer wins !!")
