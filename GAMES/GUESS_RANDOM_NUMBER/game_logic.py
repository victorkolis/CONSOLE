#!/usr/bin/env python3

from ascii_color import *
import subprocess
import random
import time

class Game:
	def __init__(self):
		self.guess = ''
		self.numbers_guessed = []
		self.chances = 5
		self.min = 1
		self.max = 20
		self.random_number = str(random.randint(self.min, self.max))
	
	def sleep(self, x=0):
		time.sleep(x)
	
	def clear(self):
		subprocess.call('clear')
		
	def three_liner(self):
		print('\n\n\n')
	
	# Intro message
	def goal(self):
		self.clear()
		self.three_liner()
		print(Color.green, f'''I AM THINKING OF A NUMBER BETWIXT {self.min} & {self.max}''')
		self.sleep()
		self.three_liner()
		
	# Game update
	def update(self):
		# Asks for user input
		self.guess = input('>>> ')
		
		# Check if the user's guess is correct
		if self.guess == self.random_number:
			self.clear()  # cleans the terminal
			self.three_liner()  # Spaces to help readability
			print(Color.red,'CONGRATULATIONS!!') 
			self.three_liner()
			self.sleep()
			
			# Checks if user wants to play again
			if self.restart() == 'n':
				self.clear()
				return True
			else:
				self.clear()
				self.goal()
				self.random_number = str(random.randint(self.min, self.max))
				self.chances = 5
		
		else:
			self.chances -= 1
			
		if self.chances == 0:
			self.game_over()
		
	def restart(self):
		self.three_liner()
		print(Color.cyan, 'Play again? (y/n)', end='')
		return input(': ')
	
	def game_over(self):
		self.clear()
		self.three_liner()
		print(Color.red, 'GAME OVER')
		self.sleep()
		self.clear()
		self.three_liner()
		print(Color.red, f'THE CORRECT NUMBER WAS {self.random_number}')
		self.sleep()
		self.clear()
		
		# Checks if user wants to play again
		# Ends the game
		if self.restart() == 'n':
			self.clear()
			self.goodbye()
			

		else:
			# Restarts the game
			self.clear()
			self.goal()
			self.random_number = str(random.randint(self.min, self.max))
			self.chances = 5

	def goodbye(self):
		for letter in 'SEE YOU LATER THEN':
			print(letter)
			self.sleep(0.2)
		self.clear()
