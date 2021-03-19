###############################
# Author : Code Future Invent #
# Version: 1.0.0              #
# Date	 : Mar-19-2020	      #
###############################

#!/usr/bin/env python3

from game_logic import Game

# Assets
game = Game()
game.goal()

# Game Loop
while True:
	if game.update() == True:
		break
