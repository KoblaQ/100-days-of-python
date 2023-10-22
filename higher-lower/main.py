import random
from art import logo, vs
from game_data import data
import os


def play_game():
    print(logo)

    end_game = False
    score = 0
    #To help reusing the last highest value
    compare = random.choice(data)
    against = random.choice(data)


    def compare_values(compare, against):
        #Compare the two follower counts
        #if compare['follower_count'] > against['follower_count']:
        if compare > against:
            return "a"
        else:
            compare = against
            return "b"

    while not end_game:
        #Get random values from data.
        compare = against
        #against = data[random.randint(0,len(data))]
        against = random.choice(data)
        
        # check and correct if the values were the same.
        while compare == against:
            against = random.choice(data)

        print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
        print(vs)
        print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
       
        #Check to see if the the answer is correct
        if answer == compare_values(compare['follower_count'],against['follower_count']):
            score += 1
            print(f"You're rignt! Current score: {score}. ")
        else:
            #clear screen first 
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            end_game = True

play_game()
