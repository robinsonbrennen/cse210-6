import random
from enum import IntEnum

class Input(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

win = {
    Input.Scissors: [Input.Lizard, Input.Paper], Input.Paper: [Input.Spock, Input.Rock], Input.Rock: [Input.Lizard, Input.Scissors], Input.Lizard: [Input.Spock, Input.Paper], Input.Spock: [Input.Scissors, Input.Rock]
}

def pick_winner(user_pick, computer_pick):
    defeats = win[user_pick]
    if user_pick == computer_pick:
        print(f"Both players selected {user_pick.name}. It's a tie!")
    elif computer_pick in defeats:
        print(f"{user_pick.name} beats {computer_pick.name}! You win!")
    else:
        print(f"{computer_pick.name} beats {user_pick.name}! You lose.")

def computer_input():
    selection = random.randint(0, len(Input) - 1)
    action = Input(selection)
    return action

def user_input():
    choices = [f"{action.name}[{action.value}]" for action in Input]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Input(selection)
    return action

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
