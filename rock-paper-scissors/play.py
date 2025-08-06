import random

def get_player_choice():
    """Gets and validates the player's choice."""
    while True:
        choice = input("Choose your weapon! (rock 🪨, paper 📄, scissors ✂️): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the round."""
    if player_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!" 
    else:
        return "You lose!"

def play_game():
    """Runs a single round of the Rock Paper Scissors game."""
    print("\n--- Rock Paper Scissors with Emojis! ---")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {player_choice} " + {"rock":"🪨 ", "paper":"📄", "scissors":"✂️"}[player_choice])
    print(f"Computer chose: {computer_choice} " + {"rock":"🪨", "paper":"📄 " , "scissors":"✂️"}[computer_choice])

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! 👋")

            break