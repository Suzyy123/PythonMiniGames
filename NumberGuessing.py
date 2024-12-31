#Concepts Covered: Random numbers, loops, conditionals, user input
import random
number = random.randint(1,10)
gameStart = True

while gameStart:
    userInput = int(input("Guess a number: "))
    if userInput < number:
      
        print("Too small")
    elif userInput > number:
      
        print("Too high")
    else:
    
        print("Correct! The number is"+ str(number))
        gameStart = False
       
