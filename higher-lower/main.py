import random
from art import logo, vs
from game_data import data
import os


def play_game():
    print(logo)

    end_game = False
    score = 0

    def compare_values():
        #Compare the two follower counts
        if compare['follower_count'] > against['follower_count']:
            return "A"
        else:
            return "B"

    while not end_game:
        #Get random values from data.
        compare = data[random.randint(0,len(data))]
        against = data[random.randint(0,len(data))]
        print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
        print(vs)
        print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ")
       

        if answer == compare_values():
            score += 1
            print(f"You're rignt! Current score: {score}. ")
        else:
            #clear screen first 
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            end_game = True

play_game()
