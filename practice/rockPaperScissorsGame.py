# import random
# gameList = ["rock", "paper", "scissors"]
# print("Let's play. Y/n?")
# mood = input("Enter y for yes, n for no: ")
# while(mood == 'y'):
#     choice = random.choice(gameList)
#     print("r: rock, p: paper, s: scissors")
#     try:
#         userChoice = input("Please enter your choice? r,p,s: ")
#     except Exception as e:
#         print("Please input correct choice", str(e))
#     else: 
#         if(userChoice == choice):
#             print("Tie! No Winner.")
#         elif(userChoice == 'r' and choice == gameList[1]):
#             print("Opponent: Paper. You Lost!")
#         elif(userChoice == 'r' and choice == gameList[2]):
#             print("Opponent: Scissors. You Won!")
#         elif(userChoice == 'p' and choice == gameList[0]):
#             print("Opponent: Rock. You Won!")
#         elif(userChoice == 'p' and choice == gameList[2]):
#             print("Opponent: Scissors. You Lost!")
#         elif(userChoice == 's' and choice == gameList[1]):
#             print("Opponent: Paper. You Won!")
#         elif(userChoice == 's' and choice == gameList[0]):
#             print("Opponent: Rock. You Lost!")
#         else:
#             pass
#     try:
#         mood = input("Do you want to play again? y/n: ")
#     except Exception as e:
#         print("Please input correct choice for mood", str(e))

import random
while True:
    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)
    player = None

    while player not in choices:
        player = input ("rock, paper or scissors?: ").lower()

        if player == computerChoice:
                print("computer: ", computerChoice)
                print("user: ", player)
                print("TIE!")
        elif player == "rock":
            if computerChoice == "paper":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You LOST!")
            if computerChoice == "scissors":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You WIN!")
        elif player == "paper":
            if computerChoice == "scissors":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You LOST!")
            if computerChoice == "rock":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You WIN!")
        elif player == "scissors":
            if computerChoice == "rock":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You LOST!")
            if computerChoice == "paper":
                print("computer: ", computerChoice)
                print("user: ", player)
                print("You WIN!")
    play_again = input("Play again? (y/n): ").lower()
    
    if (play_again != "yes"):
        break
print("Bye!")


    
  


         