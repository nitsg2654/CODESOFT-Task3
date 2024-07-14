import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def playing():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = game(user_choice, computer_choice)
    
    print("You choose: ", user_choice)
    print("Computer choose: ", computer_choice)
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")
    
    return result

def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"
    
    while play_again.lower() in ["yes", "y"]:
        result = playing()
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print("Score - You: ", user_score, "Computer: ", computer_score)
        
        play_again = input("Do you want to play again? (yes or no): ")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
