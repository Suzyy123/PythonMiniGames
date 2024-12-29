import random
# how you want the hangman

def hangman_display(stage):
    stages = [
        """
           +---+
               |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
           |   |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|   |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
               |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
          /    |
               |
               |
        =========
        """,
        """
           +---+
           O   |
          /|\\  |
          / \\  |
               |
               |
        =========
        """,
    
    ]
    print(stages[stage])

# creating a hashmap for word guessing game
print( "HangMan" )
guessing_word = ["python", "javascript", "Programmer", "java", "flutter"]
game_over = False
# program chooses the word
choose_word = random.choice(guessing_word).lower()
print("The word is of " + str(len(choose_word)) + " letters")

# attempts
attempts = len(choose_word) + 2
wrong_attempts = 0
hidden_words = ["_"] * len(choose_word) 
print(" ".join(hidden_words))

while not game_over:
    hangman_display(wrong_attempts)
    guessing_letter = input("Guess a letter: ").lower() 

    if guessing_letter in choose_word:
        for position in range(len(choose_word)):
            if choose_word[position] == guessing_letter:
                hidden_words[position] = guessing_letter
        print(" ".join(hidden_words))
    else:
        print("Wrong guess")
        wrong_attempts += 1
        attempts -= 1

    if wrong_attempts == 6:  
        hangman_display(6)  # Display the final hangman
        print("You lose! The correct word was " + choose_word)
        game_over = True

    if "_" not in hidden_words:
        game_over = True
        print("Correct! The word is " + choose_word)
