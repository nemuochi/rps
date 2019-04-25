#!/usr/bin/env python3
# referenced from "Knowledge" answers in Udacity nanodegree program
# https://knowledge.udacity.com/?nanodegree=5d1543a2-496f-11e8-b51b-238bfb35bf1b&project=97abcd48-83f2-11e8-a3d3-572e59a979e4

import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# Player only returns 'rock'.
class Player:
    my_move = "None"
    their_move = "None"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# Random player subclass
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human player(you) subclass
class HumanPlayer(Player):
    def move(self):
        # while True:
        #     choice = input(
        #             "Rock, paper, scissors? (quit to 'q')>").lower().strip()
        #     if choice == "q":
        #         print_pause("bye")
        #         exit(0)
        #     elif choice in moves:
        #         return choice
        #     else:
        #         print_pause(f"I don't understand. Choose: {' '.join(moves)}?")
        move = input("ROCK, PAPER or SCISSORS ?").lower()
        while move not in moves:
           print("Invalid choice, try again")
           move = input("ROCK, PAPER or SCISSORS ?").lower()
        return move

# subclass for reflect player(imitate your previous move)
class ReflectPlayer(Player):  # imitate your move
    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        else:
            return self.their_move


# subclass for cycle player (cycle through the move regularly)
class CyclePlayer(Player):
    def move(self):
        if self.my_move == "None":
            return random.choice(moves)
        if self.my_move == "rock":
            return moves[2]  # "scissors"
        elif self.my_move == "paper":
            return moves[0]  # "rock"
        else:
            return moves[1]  # "paper"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  You: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # Keeping scores of p1 and p2:
        if move1 == move2:
            print_pause("it's tie")
        elif beats(move1, move2) is True:
            self.p1.score += 1
            print_pause("Player1 has won")
        elif beats(move2, move1) is True:
            self.p2.score += 1
            print_pause("You(Player2) has won")
        print(f"Player 1: {self.p1.score} You: {self.p2.score}")

    def play_game(self):
        print_pause("Game start!")
        print_pause("Rock Paper Scissors, Go!")
        round = 1
        # Game over when a player is ahead by 3 points.
        while self.p1.score <= 3:
            if self.p1.score == 3:
                print_pause("Game over! You lost!")
                print_pause(f"Final score\t*{self.p1.score} : {self.p2.score}")
                game.playagain()
            elif self.p2.score == 3:
                print_pause("Game over! You won!")
                print_pause(f"Final score\t*{self.p2.score} : {self.p1.score}")
                game.playagain()
            else:
                print(f"Round {round}: ")
                self.play_round()
            round += 1

    # Will you play again?
    def playagain(self):
        # Change the terminal display: white with purple background color
        print("\033[1;37;45m \n")
        choice = input("Would you like to play again? (Y/N)").lower().strip()
        if choice == 'y':   # Yes, I play again.
            print_pause("Excellent! Restarting the game ...\n")
            self.p1.score = 0  # Reset the score.
            self.p2.score = 0  # Reset the score.
            print("\033[1;32;40m \n")  # Change the terminal color to play mode
            self.play_game()
        else:  # No, I quit.
            print_pause("Thanks for playing! See you next time.")
            exit(0)


if __name__ == '__main__':
    # Change the terminal display: bright green with black background color
    print("\033[1;32;40m \n")
    # dictionary for opponent's list.
    d = {
         1: Player(),
         2: RandomPlayer(),
         3: ReflectPlayer(),
         4: CyclePlayer()
    }
    # Before playing the game, choose your opponent.
    chooseplayer = int(input("Choose your player: 1, 2, 3 or 4\n"))
    opponent = d[chooseplayer]
    you = HumanPlayer()
    game = Game(opponent, you)
    game.play_game()
