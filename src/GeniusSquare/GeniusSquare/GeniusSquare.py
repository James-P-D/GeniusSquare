import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *
import threading
from random import randint
import time

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

grid = np.zeros([COLS, ROWS])

# Global flags
rolling_dice = False
solving = False

###############################################
# initialise()
###############################################

def initialise():
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

    clear_grid()

###############################################
# clear_grid()
###############################################

def clear_grid():
    for col in range(COLS):
        for row in range(ROWS):            
            grid[col, row] = CELL_EMPTY

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
# roll_dice()
###############################################

def roll_dice():
    rolling_dice = True
    clear_grid()
    thread = threading.Thread(target = roll_dice_on_thread, args = ())
    thread.start()                    

###############################################
# roll_dice_on_thread()
###############################################

def roll_dice_on_thread():
    dice_roll_counter = np.zeros(TOTAL_DICE)
    for i in range(len(dice_roll_counter)):
        if (i == 0):
            dice_roll_counter[i] = int(randint(1, 1))
        else:
            dice_roll_counter[i] = dice_roll_counter[i - 1] + int(randint(1, 1))

    while dice_roll_counter[-1] != 0:
        for i in range(len(dice_roll_counter)):
            if (dice_roll_counter[i] > 0):
                dice_roll_counter[i] -= 1
                dice_strip[i].inc_value()
                dice_strip[i].draw(screen)
        time.sleep(0.1)

    for dice in dice_strip:
        (col, row) = dice.get_value()
        grid[col, row] = CELL_BLOCKED
    
    draw_grid()
    print(dice_roll_counter)
    global rolling_dice
    rolling_dice = False

###############################################
# draw_grid()
###############################################

def draw_grid():
    for col in range(COLS):
        for row in range(ROWS):
            draw_cell(col, row, int(grid[col, row]))

###############################################
# draw_cell()
###############################################

            
def draw_cell(col, row, cell_value):
    x = GRID_LEFT + (CELL_HEIGHT * col)
    y = GRID_TOP + (CELL_WIDTH * row)
    
    if (grid[col, row] == CELL_BLOCKED):
        pygame.draw.ellipse(screen, TAN, (x+5, y+5, CELL_WIDTH-10, CELL_HEIGHT-10))
    else:
        pygame.draw.rect(screen, CELL_COLORS[cell_value], (x, y, CELL_WIDTH, CELL_HEIGHT))

###############################################
# game_loop()
###############################################

def game_loop():
    global rolling_dice
    game_exit = False
    clock = pygame.time.Clock()    

    while not game_exit:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) and (not (rolling_dice or solving)):
                game_exit = True;
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (not (rolling_dice or solving)):
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if (roll_dice_label.is_over(mouse_x, mouse_y)):
                    roll_dice()


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
    roll_dice()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()

