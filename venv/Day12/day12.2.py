#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

EASY_LEVEL=10 ##global variable
HARD_LEVEL=5 ##global variable

def check_answer(guess, answer,turns):
    if guess>answer:
        print("Too High")
        return turns-1
    elif guess<answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it. The answer is {guess}")

def set_difficulty():
    level=input("Choose Difficulty: easy or hard>> ").lower()
    if level=='easy':
      return EASY_LEVEL
    elif level=='hard':
        return HARD_LEVEL
    else:
        print("Invalid Choiche")



def game():
    print(logo)
    print("Welcome to the game")
    print("Thinking a number between 1 to 100")

    answer=randint(1,100)
    print(f"The correct answer is {answer}")
    turns=set_difficulty() ##function call


    guess=0 ##global variable
    while guess!=answer:
        print(f"You have {turns} attempts ")

        guess=int(input("Make a Guess:"))

        turns=check_answer(guess, answer,turns) ##function call and added to turns
        if turns==0: ### attept end
            print("You Lose")
            return ###use to stop function

game()