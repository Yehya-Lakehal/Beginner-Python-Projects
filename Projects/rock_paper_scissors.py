# Python Rock Paper Scissors

import random

print("===========================================")
print(" Welcome to the ROCK Paper Scisssors Game! ")

items = ["rock", "paper", "scissors"]
wins = 0
loses = 0
draws = 0
while True:
    print("===========================================")
    print("Hint: Press \"q\" to exit!")
    computer_guess = items[random.randrange(0,2)]
    print("What\'s your guess (rock, paper,scissors) ?")
    guess = input("> ").lower()
    if ((guess == "rock" and computer_guess == "scissors") or (guess == "paper" and computer_guess == "rock") or (guess == "scissors" and computer_guess == "paper")):
        print("Congratulation! You Won!")
        wins += 1
    elif ((guess == "scissors" and computer_guess == "rock") or (guess == "rock" and computer_guess == "paper") or (guess == "paper" and computer_guess == "scissors")):
        print("Unfortunetaly.. You Lose!")
        loses += 1
    elif guess == computer_guess:
        print("Draw!")
        draws += 1
    elif guess == "q":
        break
    else:
        print("Error: Invalid Input!")

print(f"--- Total ---\n- wins : {wins:02} -\n- loses: {loses:02} -\n- draws: {draws:02} -\n-------------")

print("===========================================")
