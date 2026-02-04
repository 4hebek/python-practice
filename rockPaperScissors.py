# Write a rock, paper, scissors game using functions.
# play against the computer. 
# Keep track of the score for the user + computer + draws.
# focus on using functions to make the output nice. 

# stretch: explore recursion for winning logic.


def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    import random
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"): 
        return "user"
    else:
        return "computer"
    
def play_game():
    user_score = 0
    computer_score = 0
    draw_score = 0

    rounds = int(input("Enter number of rounds to play: "))
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            draw_score += 1
            print("This round is a draw!")
        
        print(f"Score -> You: {user_score}, Computer: {computer_score}, Draws: {draw_score}\n")
    
    print("Final Scores:")
    print(f"You: {user_score}, Computer: {computer_score}, Draws: {draw_score}")
    
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer wins overall! Better luck next time.")
    else:
        print("It's an overall draw!")
        
play_game()