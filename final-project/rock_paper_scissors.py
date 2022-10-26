import random

user_wins = 0
computer_wins = 0
tie_game = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 4)
    # rock = 0 paper = 1 scissors = 2 lizard = 3 spock = 4
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Win if rock crushes scissors, rock crushes lizard
    # Lose if spock vaporizes rock, paper covers rock 
    if user_input == "rock" and computer_pick == "scissors" and computer_pick == "lizard":
        print("You won!")
        user_wins += 1

    # Win if paper covers rock, paper disproves spock
    # Lose if scissors cuts paper, lizard eats paper
    elif user_input == "paper" and computer_pick == "rock" and computer_pick == "spock":
        print("You won!")
        user_wins += 1

    # Win if scissors cuts paper, scissors decapitates lizard
    # Lose if spock smashes scissors, rock smashes scissors
    elif user_input == "scissors" and computer_pick == "paper" and computer_pick == "lizard":
        print("You won!")
        user_wins += 1

    # Win if lizard eats paper, lizard poisons spock
    # Lose if rock crushes lizard, scissors decapitates lizard
    elif user_input == "lizard" and computer_pick == "spock" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    # Win if spock smashes scissors, spock vaporizes rock
    # Lose if paper disproves spock, lizard poisons spock
    elif user_input == "spock" and computer_pick == "scissors" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("You tied", tie_game, "times.")
print("Goodbye!")
