from random import randint

#create a list of play options
l = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = l[randint(0,2)]

#set player to Falsero
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player,"smashs", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer,"cuts", player)
        else:
            print("You win!", player,"covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer,"smashes", player)
        else:
            print("You win!", player,"cuts", computer)
    else:
        print("Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = l[randint(0,2)]