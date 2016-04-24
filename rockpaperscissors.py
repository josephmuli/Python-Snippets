#!usr/bin/env python2


import random
import time

rock = 1 
paper = 2
scissors = 3

#a few rules...
names = {rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

#game start:
def start():
	print("Let's play a game of Rock, Paper, Scissors ?")
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1,3)
	result(player, computer)
	return play_again()

def move():
	while True:
		print
		player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print("Oops! I didn't unserstand that. Please enter either 1,2 or 3.")

def result(player, computer):
	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)
	print("Computer threw {0}!".format(names[computer]))