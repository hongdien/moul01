import random

# Define choices
choices = ["rock", "paper", "scissors", "lizard", "Spock"]

# Rules for winning
winning_combinations = {
    ("rock", "scissors"): "rock crushes scissors",
    ("rock", "lizard"): "rock crushes lizard",
    ("paper", "rock"): "paper covers rock",
    ("paper", "Spock"): "paper disproves Spock",
    ("scissors", "paper"): "scissors cuts paper",
    ("scissors", "lizard"): "scissors decapitates lizard",
    ("lizard", "Spock"): "lizard poisons Spock",
    ("lizard", "paper"): "lizard eats paper",
    ("Spock", "scissors"): "Spock smashes scissors",
    ("Spock", "rock"): "Spock vaporizes rock"
}

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (player_choice, computer_choice) in winning_combinations:
        return f"You win! {winning_combinations[(player_choice, computer_choice)]}"
    else:
        return f"You lose! {winning_combinations[(computer_choice, player_choice)]}"

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    
    while True:
        # Get player's choice
        player_choice = input(f"Choose one: {', '.join(choices)}: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose from rock, paper, scissors, lizard, or Spock.")
            continue
        
        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = get_winner(player_choice, computer_choice)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
