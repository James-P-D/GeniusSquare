import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *
import threading

###############################################
# Globals
###############################################

###############################################
# initialise()
###############################################

def initialise():
    pygame.display.set_caption("Genius Square")
    global dice_strip
    global grid
        
    dice_strip[0] = DiceCell(CELL_WIDTH * col, 0, CELL_WIDTH, CELL_HEIGHT, 0)

    for col in range(CELL_COLS):
        for row in range(CELL_ROWS):            
            grid[col, row] = Cell(CELL_WIDTH * col, (CELL_HEIGHT * (row + 1)), CELL_WIDTH, CELL_HEIGHT)

###############################################
# main()
###############################################

def main():
    pygame.init()
    
    initialise()
    
    # Put this line back in to run the demo game from the README.MD
    #set_default_game()

    draw_ui()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()

