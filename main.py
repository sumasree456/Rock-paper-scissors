import random
choices=["rock","paper","scissors"]
player=None
computer=random.choice(choices)

while player not in choices:
    player = input("rock,paper or scissors..?").lower()
print(computer)
if player==computer:
    print("tie..!")
elif player == "rock":
    if computer=="paper":
        print("You lost the game..!")
    elif computer=="scissors":
        print("you won")
elif player == "paper":
    if computer=="rock":
        print("You won ..!")
    elif computer=="scissors":
        print("you lost the game..!")
elif player == "scissors":
    if computer=="paper":
        print("You won the game..!")
    elif computer=="rock":
        print("you lost the game")





