import random
import sys

moves = ["rock", "paper", "scissors"]

usermove = input("What will you play?").lower()

move = random.choice(moves)


if usermove in moves:
     print("I chose:", move)
else:
    print("only rock, paper or scissors!")
    sys.exit() 

if usermove == move:
    print("It's a tie!")

elif (usermove == "rock" and move == "paper") or \
     (usermove == "paper" and move == "scissors") or \
     (usermove == "scissors" and move == "rock"):
    print("You lose!")

else:
    print("You win!")