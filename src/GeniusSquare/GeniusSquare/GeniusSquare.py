import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *
import threading
import random
import time

###############################################
# Globals
###############################################

# pygame screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Label at top
roll_dice_label = Label(0, 0, ROLL_DICE_LABEL_WIDTH, ROLL_DICE_LABEL_HEIGHT, "ROLL DICE")

# Strip for 7 dice
dice_strip = np.ndarray(TOTAL_DICE, DiceCell)

# Column labels (1-6)
col_labels = np.ndarray(COLS, Label)

# Row labels (A-F)
row_labels = np.ndarray(ROWS, Label)

# Solve label at bottom
solve_label = Label(0, SOLVE_LABEL_TOP, SOLVE_LABEL_WIDTH, SOLVE_LABEL_HEIGHT, "SOLVE")

# Actual grid
grid = np.zeros([COLS, ROWS])

# Global flags
rolling_dice = False
solving = False

###############################################
# initialise()
###############################################

def initialise():
    pygame.display.set_caption("Genius Square")
    random.seed(time.perf_counter)
    
    global dice_strip
    global grid

    for i in range(TOTAL_DICE):
        dice_strip[i] = DiceCell(CELL_WIDTH * (i + 1), DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_VALUES[i])
    for i in range(COLS):
        col_labels[i] = Label(CELL_WIDTH * (i + 1), COL_LABEL_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, get_col_label(i))
    for i in range(ROWS):
        row_labels[i] = Label(0, ROLL_DICE_LABEL_HEIGHT + DICE_STRIP_HEIGHT + ((i + 1) * CELL_HEIGHT), CELL_WIDTH, CELL_HEIGHT, get_row_label(i))

    clear_whole_grid()

###############################################
# clear_grid()
###############################################

def clear_whole_grid():
    for col in range(COLS):
        for row in range(ROWS):            
            grid[col, row] = CELL_EMPTY

###############################################
# clear_grid(cell_type)
###############################################

def clear_grid(cell_type):
    for col in range(COLS):
        for row in range(ROWS):            
            grid[col, row] = CELL_EMPTY if grid[col, row] == cell_type else grid[col, row]

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
# solve()
###############################################

def solve():
    global solving
    solving = True    
    thread = threading.Thread(target = solve_on_thread, args = ())
    thread.start()                    

###############################################
# solve_on_thread()
###############################################

def solve_on_thread():

    ###############################################
    # sub_solve()
    ###############################################

    def sub_solve(cell_type_index):

        ###############################################
        # piece_fits()
        ###############################################
        def piece_fits(piece_shape, piece_cols, piece_rows, col, row):
            for piece_col in range(piece_cols):
                for piece_row in range(piece_rows):
                    if ((grid[col + piece_col][row + piece_row] != CELL_EMPTY) and (piece_shape[piece_col][piece_row] != CELL_EMPTY)):
                        return False
            return True

        ###############################################
        # add_piece()
        ###############################################
        def add_piece(piece_shape, piece_cols, piece_rows, col, row):
            for piece_col in range(piece_cols):
                for piece_row in range(piece_rows):
                    if (piece_shape[piece_col][piece_row] != CELL_EMPTY):
                        grid[col + piece_col][row + piece_row] = piece_shape[piece_col][piece_row]            

        piece_shapes = PIECE_SHAPES[cell_type_index];

        for piece_shape in piece_shapes:
            piece_cols = len(piece_shape)
            piece_rows = len(piece_shape[0])

            for col in range(0, COLS - piece_cols + 1):
                for row in range(0, ROWS - piece_rows + 1):
                    if (piece_fits(piece_shape,  piece_cols, piece_rows, col, row)):
                        add_piece(piece_shape, piece_cols, piece_rows, col, row)
                        draw_grid()
                        time.sleep(SLEEP_DELAY)
                        if (cell_type_index == 0):
                            return True
                        else:
                            if (sub_solve(cell_type_index - 1)):
                                return True
                        clear_grid(cell_type_index + 1)
                        draw_grid()
                        time.sleep(SLEEP_DELAY)                        
        return False                        
            
    if(sub_solve(len(PIECE_SHAPES) - 1)):
        print("Solved!")
    else:
        print("No Solution Found!")

    global solving
    solving = False

###############################################
# roll_dice()
###############################################

def roll_dice():
    global rolling_dice
    rolling_dice = True
    clear_whole_grid()
    draw_grid()
    thread = threading.Thread(target = roll_dice_on_thread, args = ())
    thread.start()                    

###############################################
# roll_dice_on_thread()
###############################################

def roll_dice_on_thread():
    
    dice_roll_counter = np.zeros(TOTAL_DICE)
    for i in range(len(dice_roll_counter)):
        if (i == 0):
            dice_roll_counter[i] = int(random.randint(0, 6))
        else:
            dice_roll_counter[i] = dice_roll_counter[i - 1] + int(random.randint(0, 6))

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
        pygame.draw.ellipse(screen, TAN, (x + BORDER_SIZE, y + BORDER_SIZE, CELL_WIDTH - (2 * BORDER_SIZE), CELL_HEIGHT - (2 * BORDER_SIZE)))
    else:
        pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT))
        pygame.draw.rect(screen, CELL_COLORS[cell_value], (x + BORDER_SIZE, y + BORDER_SIZE, CELL_WIDTH - (2 * BORDER_SIZE), CELL_HEIGHT - (2 * BORDER_SIZE)))

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
                if (solve_label.is_over(mouse_x, mouse_y)):
                    solve()

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

