#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

games=[]

def Random():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def Rock(opc):
    opponent = Random()
    if opponent == "rock":
        AddGame("Tie")
        print("Tie")
        again()
    elif opponent == "paper":
        AddGame("Loser")
        print("Loser")
        again()
    elif opponent == "scissors":
        AddGame("Winner")
        print("Winner")
        again()

def Paper(opc):
    opponent = Random()
    if opponent == "rock":
        AddGame("Winner")
        print("Winner")
        again()
    elif opponent == "paper":
        AddGame("Tie")
        print("Tie")
        again()
    elif opponent == "scissors":
        AddGame("Loser")
        print("Loser")
        again()

def Scissors(opc):
    opponent = Random()
    if opponent == "rock":
        AddGame("Loser")
        print("Loser")
        again()
    elif opponent == "paper":
        AddGame("Winner")
        print("Winner")
        again()
    elif opponent == "scissors":
        AddGame("Tie")
        print("Tie")
        again()

def AddGame(gif):
    games.append(gif)

def again():
    opc = str(input("Do you want to play again? (y/n): "))
    if opc == "y":
        Game()
    elif opc == "n":
        count_games = len(games)
        won_games=games.count("Winner")
        print("You played", count_games, "games and won", won_games, "of them.")
    else:
        print("Invalid option. Try again.")
        again()

def Game():
    print("""***********************
Welcome to Rock, Paper, Scissors!
***********************
Write your choice:
rock
paper
scissors      
    """)
    opc = str(input("Your choice: "))
    new_opc = opc.lower()
    if new_opc == "rock":
        Rock(new_opc)
    elif new_opc == "paper":
        Paper(new_opc)
    elif new_opc == "scissors":
        Scissors(new_opc)
    else:
        print("Invalid option. Try again.")
        Game()

Game()