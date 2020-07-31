import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *
import threading

###############################################
# Globals
###############################################

# pygame screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

roll_dice_label = Label(0, 0, ROLL_DICE_LABEL_WIDTH, ROLL_DICE_LABEL_HEIGHT, "ROLL DICE")
dice_strip = np.ndarray(TOTAL_DICE, DiceCell)
col_labels = np.ndarray(COLS, Label)
row_labels = np.ndarray(ROWS, Label)
solve_label = Label(0, SOLVE_LABEL_TOP, SOLVE_LABEL_WIDTH, SOLVE_LABEL_HEIGHT, "SOLVE")

# Global flags
processing = False

###############################################
# initialise()
###############################################

def display_it(l):
    ret_val = ""
    for (a, b) in l:
        x = int(b) - 1
        y = -1
        if (a == "A"):
            y = 0
        elif (a == "B"):
            y = 1
        elif (a == "C"):
            y = 2
        elif (a == "D"):
            y = 3
        elif (a == "E"):
            y = 4
        elif (a == "F"):
            y = 5
        ret_val = ret_val + "(" + str(x) + ", " + str(y) + "),"
    print(ret_val)

def initialise():

    display_it(["A1", "C1", "D1", "D2", "E2", "F2"])
    display_it(["A5", "F2", "A5", "F2", "B6", "E1"])
    display_it(["A4", "B5", "C5", "C6", "D6", "F6"])
    display_it(["F5", "E5", "F4", "D5", "E4", "E6"])
    display_it(["C3", "C4", "D3", "B4", "D4", "E3"])
    display_it(["B2", "A2", "A3", "B1", "B3", "C2"])
    display_it(["F1", "A6", "A6", "A6", "F1", "F1"])

    pygame.display.set_caption("Genius Square")

    global dice_strip
    global grid
        
    dice_strip[0] = DiceCell(CELL_WIDTH * 1, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_0_VALUES)
    dice_strip[1] = DiceCell(CELL_WIDTH * 2, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_1_VALUES)
    dice_strip[2] = DiceCell(CELL_WIDTH * 3, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_2_VALUES)
    dice_strip[3] = DiceCell(CELL_WIDTH * 4, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_3_VALUES)
    dice_strip[4] = DiceCell(CELL_WIDTH * 5, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_4_VALUES)
    dice_strip[5] = DiceCell(CELL_WIDTH * 6, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_5_VALUES)
    dice_strip[6] = DiceCell(CELL_WIDTH * 6, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_6_VALUES)

    for i in range(COLS):
        col_labels[i] = Label(CELL_WIDTH * (i + 1), COL_LABEL_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, get_col_label(i))
    for i in range(ROWS):
        row_labels[i] = Label(0, ROLL_DICE_LABEL_HEIGHT + DICE_STRIP_HEIGHT + ((i + 1) * CELL_HEIGHT), CELL_WIDTH, CELL_HEIGHT, get_row_label(i))



    #for col in range(CELL_COLS):
    #    for row in range(CELL_ROWS):            
    #        grid[col, row] = Cell(CELL_WIDTH * col, (CELL_HEIGHT * (row + 1)), CELL_WIDTH, CELL_HEIGHT)

###############################################
# draw_ui()
###############################################

def draw_ui():
    roll_dice_label.draw(screen)
    for dice in dice_strip:
        dice.draw(screen)
    for col_label in col_labels:
        col_label.draw(screen)
    for row_label in row_labels:
        row_label.draw(screen);
    solve_label.draw(screen)

###############################################
# game_loop()
###############################################

def game_loop():
    game_exit = False
    clock = pygame.time.Clock()
    while not game_exit:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) and (not processing):
                game_exit = True;
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (not processing):
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()

###############################################
# main()
###############################################

def main():
    pygame.init()
    
    initialise()

    draw_ui()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()

