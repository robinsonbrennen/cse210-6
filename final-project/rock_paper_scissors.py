import random
from enum import IntEnum

# Create class input and use intenum to create enumerated constants
class Input(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

# Add all of the winning actions
win = {
    Input.Scissors: [Input.Lizard, Input.Paper], Input.Paper: [Input.Spock, Input.Rock], Input.Rock: [Input.Lizard, Input.Scissors], Input.Lizard: [Input.Spock, Input.Paper], Input.Spock: [Input.Scissors, Input.Rock]
}

# Create a dictionary to define the ways to win
def pick_winner(user_pick, computer_pick):
    defeats = win[user_pick]
    if user_pick == computer_pick:
        print(f"You both picked {user_pick.name}. It's a tie!")
    elif computer_pick in defeats:
        print(f"{user_pick.name} beats {computer_pick.name}! You win!")
    else:
        print(f"{computer_pick.name} beats {user_pick.name}! You lose.")

# Get input from the computer at random
def computer_input():
    selection = random.randint(0, len(Input) - 1)
    pick = Input(selection)
    return pick

# Get input from user
def user_input():
    choices = [f"{pick.name}[{pick.value}]" for pick in Input]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    pick = Input(selection)
    return pick

# While loop to direct the game, check for valid input, and ask user if they want to play again
while True:
    try:
        user_pick = user_input()
    except ValueError as e:
        range_str = f"[0, {len(Input) - 1}]"
        print(f"Incorrect input. Enter {range_str}")
        continue

    computer_pick = computer_input()
    pick_winner(user_pick, computer_pick)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
