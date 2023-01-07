import random
from art import logo

Easy_level = 10
Hard_level = 5
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return Easy_level
  else:
    return Hard_level

def game():
  print(logo)
  print("welcome to number guessing game")
  print("choose between 1 to 100.")
  answer = random.randint(1, 100)

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"Hey, you have {turns} chances remaining to guess the number for  winning.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
