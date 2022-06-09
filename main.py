import random

while True:

    choices = ["rock","paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()
        print("Error!!! choose from the given options")

    if player == computer:
            print("computer: ",computer)
            print("player: ",player)
            print("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry, you've lost the game!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Hurray!!! you've WON")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry, you've lost the game!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Hurray!!! you've WON")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry, you've lost the game!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Hurray!!! you've WON")

    play_again = input("Play again? (yes/no): ").lower ()

    if play_again != "yes":
        break
print("Goodbye!")           
