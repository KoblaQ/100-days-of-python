#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

#Welcome message and set difficulty
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  turns = 10
elif difficulty == 'hard':
  turns = 5 
#Generate random number from 1 - 100
number = random.randint(1,101)

while turns > 0:
  print(f"You have {turns} guesses to get the number correct.")
  #Guess prompt
  guess = int(input("Make a guess: "))

  #Check if numbers are the same or higher or lower.
  if guess == number:
    print("You guessed it! The number was", number)
    break
  elif guess > number:
    print("Too high.")
  elif guess < number:
    print("Too low.")
    
  turns -= 1
  if turns == 0:
    print("Too bad, you have ran out of turns. The number was", number)

  print("Guess again.")
  
  
 