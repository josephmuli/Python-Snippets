#!usr/bin/env python2

from Tkinter import *
from ttk import *
import random
# import time


def gui():
	rock = 1 
	paper = 2
	scissors = 3

	#a few rules...
	names = {rock: "Rock", paper: "Paper", scissors: "Scissors" }
	rules = {rock: scissors, paper: rock, scissors: paper}

#game start:
	def start():
		while game():
			pass

	def game():
		player = player_choice.get()
		computer = random.randint(1,3)
		computer_choice.set(names[computer])
		result(player, computer)


	def result(player, computer):
		new_score = 0
		if player == computer:
			result_set.set("Tie game.")
		else:
			if rules[player] == computer:
				result_set.set("Your victory has been assured Mortal!")
				new_score = player_score.get()
				new_score += 1
				player_score.set(new_score)
			else:
				result_set.set("The computer laughs, you have been defeated!")
				new_score += 1
				computer_score.set(new_score)

	rps_window = Toplevel()
	rps_window.title("Rock, Paper, Scissors")

	player_choice = IntVar()
	computer_choice = StringVar()
	result_set = StringVar()
	player_choice.set(1)
	player_score = IntVar()
	computer_score = IntVar()


	rps_frame = Frame(rps_window, padding = '3 3 12 12', width = 300)





	def play_again():
		answer = raw_input("Would you like to paly again? y/n:")
		if answer in ("y", "Y", "yes", "Yes", "Of course!"):
			return answer
		else:
			print("Thank you for playing the game, you could go on, or are you scared?")



if __name__ == '__main__':
	start()