import random

# Game options
game = ["✌️", "✋", "✊"]

# Game loop
gameOver = False

while not gameOver:
    # Bot makes a random choice
    bot_choice = random.choice(game)
    # Get player's choice
    player_input = input("Scissor, Paper, Rock! Enter your choice: ").strip().lower()
    # Map player's input to emoji
    if "scissor" in player_input:
        player_choice = "✌️"
    elif "paper" in player_input:
        player_choice = "✋"
    elif "rock" in player_input:
        player_choice = "✊"
    else:
        print("Invalid choice. Please try again!")
        continue  # Restart the loop for valid input
        # Show choices
    print(f"Bot: {bot_choice}")
    print("Bot " + str(bot_choice))
    print("You " + str(player_choice))

    # Determine the result
    if player_choice == bot_choice:
        print("DRAW! No one wins.")
    elif (player_choice == "✌️" and bot_choice == "✋") or \
         (player_choice == "✋" and bot_choice == "✊") or \
         (player_choice == "✊" and bot_choice == "✌️"):
        print("You WIN 😙")
    else:
        print("You loose! ")
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes" and "y":
        gameOver = True
        print("Thanks for playing!")
