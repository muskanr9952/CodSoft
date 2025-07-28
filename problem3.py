import random
print(" Welcome to Muskan's Rock-Paper-Scissors Game!")

# Score tracking
user_score = 0
computer_score = 0 

# Choices
choices = ["rock", "paper", "scissors"]

while True:
    print("\n Choose rock, paper, or scissors(or type 'exit' to quit):")
    user_choice = input("Your choice:").lower()

    if user_choice == "exit":
        print("Game Over!")
        print("Final Score- You:", user_score, "| Computer:", computer_score)
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, scissors.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif(
       (user_choice == "rock" and 
    computer_choice == "scissors") or
       (user_choice == "paper" and 
    computer_choice == "rock") or
       (user_choice == "scissors" and
    computer_choice == "paper")
    ):
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: You lose.")
        computer_score += 1
    
    # Display Score after each round
    print("Current Score- You:", user_score, "| computer:", computer_score)