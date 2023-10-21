import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print("You chose")
if userInput == 0:
  print(rock)
elif userInput == 1:
  print(paper)
elif userInput == 2:
  print(scissors)
  
computerChoice = random.randint(0,2)

print("Computer chose")

if computerChoice == 0:
  print(rock)
elif computerChoice == 1:
  print(paper)
elif computerChoice == 2:
  print(scissors)
  


# If user chose ROCK
if userInput == 0:
  if computerChoice == 0:
    print("It's a DRAW!")
  elif computerChoice == 1:
    print("You LOSE!")
  elif computerChoice == 2:
    print("You WIN!")

# If user chose paper
if userInput == 1:
  if computerChoice == 0:
    print("You WIN!")
  elif computerChoice == 1:
    print("It's a DRAW!")
  elif computerChoice == 2:
    print("You LOSE!")

# If user chose scissors
if userInput == 2:
  if computerChoice == 0:
    print("You LOSE!")
  elif computerChoice == 1:
    print("You WIN!")
  elif computerChoice == 2:
    print("It's a DRAW!")
