# Python Guessing Game

import random

print("=========================================")
print(" Welcome to the best Guessing Game Ever! ")
print("=========================================")

min = 0
max = 0
chances = 0

while True:
    print("--------------- Difficulty --------------")
    print("1- Easy. 2- Normal. 3- Hard. 4- Imposible")     
    difficulty = int(input("Enter difficulty(1,2,3 or 4): "))
    if difficulty == 1:
        max = 10
        chances = 3
    elif difficulty == 2:
        max = 50
        chances = 5
    elif difficulty == 3:
        max = 100
        chances = 7
    elif difficulty == 4:
        max = 1000
        chances = 10
    else:
        print("Error: Invalid Input!")
        continue
    print("-----------------------------------------")
    break

computer_guess = random.randrange(min, max)
while True:
    print("------------------ Game -----------------")
    guess = int(input("Enter Your Guess: "))
    if guess == computer_guess:
        print("Congratulation! You won!")
    else:
        chances -= 1
        print(f"Your guess is false. You have {chances} chances.")
    if chances == 0:
        print(f"Unfortunataly! You lose! Computer choose {computer_guess}")
        break
    print("-----------------------------------------")

print("=========================================")
