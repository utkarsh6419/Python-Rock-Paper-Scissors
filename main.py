"""A one-round rock, paper, scissors game."""

import random

CHOICES = ("rock", "paper", "scissors")


def main():
    player = input("Choose rock, paper, or scissors: ").strip().lower()
    if player not in CHOICES:
        print("That is not a valid choice.")
        return
    computer = random.choice(CHOICES)
    print(f"Computer chose {computer}.")
    if player == computer:
        print("It is a draw.")
    elif (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
        print("You win!")
    else:
        print("Computer wins.")


if __name__ == "__main__":
    main()
