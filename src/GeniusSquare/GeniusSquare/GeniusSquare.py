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

# Column labels (1-6)
col_labels = np.ndarray(COLS, Label)

# Row labels (A-F)
row_labels = np.ndarray(ROWS, Label)

# Solve label at bottom
solve_label = Label(0, SOLVE_LABEL_TOP, SOLVE_LABEL_WIDTH, SOLVE_LABEL_HEIGHT, "SOLVE")

###############################################
# initialise()
###############################################

def initialise(dice_strip, grid):
    pygame.display.set_caption("Genius Square")
    random.seed(time.perf_counter())

    for i in range(TOTAL_DICE):
        dice_strip[i] = DiceCell(CELL_WIDTH * i, DICE_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, DICE_VALUES[i])
    for i in range(COLS):
        col_labels[i] = Label(CELL_WIDTH * (i + 1), COL_LABEL_STRIP_TOP, CELL_WIDTH, CELL_HEIGHT, get_col_label(i))
    for i in range(ROWS):
        row_labels[i] = Label(0, ROLL_DICE_LABEL_HEIGHT + DICE_STRIP_HEIGHT + ((i + 1) * CELL_HEIGHT), CELL_WIDTH, CELL_HEIGHT, get_row_label(i))

    clear_whole_grid(grid)

###############################################
# clear_grid()
###############################################

def clear_whole_grid(grid):
    for col in range(COLS):
        for row in range(ROWS):            
            grid[col, row] = CELL_EMPTY

###############################################
# clear_grid(cell_type)
###############################################

def clear_grid(grid, cell_type):
    for col in range(COLS):
        for row in range(ROWS):            
            grid[col, row] = CELL_EMPTY if grid[col, row] == cell_type else grid[col, row]

###############################################
# draw_ui()
###############################################

def draw_ui(dice_strip):
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

def solve(grid, solved, solving):
    if (get_total_blockers(grid) != TOTAL_DICE):
        print("Incorrect number of blockers!")
        return

    if (not solved):
        solving = True    
        thread = threading.Thread(target = solve_on_thread, args = (grid, solving, solved))
        thread.start()                    

###############################################
# solve_on_thread()
###############################################

def solve_on_thread(grid, solving, solved):

    ###############################################
    # sub_solve()
    ###############################################

    def sub_solve(grid, cell_type_index, solved):

        ###############################################
        # piece_fits()
        ###############################################
        def piece_fits(grid, piece_shape, piece_cols, piece_rows, col, row):
            for piece_col in range(piece_cols):
                for piece_row in range(piece_rows):
                    if ((grid[col + piece_col][row + piece_row] != CELL_EMPTY) and (piece_shape[piece_col][piece_row] != CELL_EMPTY)):
                        return False
            return True

        ###############################################
        # add_piece()
        ###############################################
        def add_piece(grid, piece_shape, piece_cols, piece_rows, col, row):
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
                    if (piece_fits(grid, piece_shape,  piece_cols, piece_rows, col, row)):
                        add_piece(grid, piece_shape, piece_cols, piece_rows, col, row)
                        draw_grid(grid)
                        time.sleep(SLEEP_DELAY)
                        if (cell_type_index == 0):
                            return True
                        else:
                            if (sub_solve(grid, cell_type_index - 1, solved)):
                                return True
                        clear_grid(grid, cell_type_index + 1)
                        draw_grid(grid)
                        time.sleep(SLEEP_DELAY)                        
        return False                        
            
    if(sub_solve(grid, len(PIECE_SHAPES) - 1, solved)):
        solved = True
        print("Solved!")
    else:
        print("No Solution Found!")

    solving = False

###############################################
# roll_dice()
###############################################

def roll_dice(grid, dice_strip, rolling_dice, solved):
    rolling_dice = True
    solved = False

    clear_whole_grid(grid)
    draw_grid(grid)
    thread = threading.Thread(target = roll_dice_on_thread, args = (dice_strip, grid, rolling_dice))
    thread.start()                    

###############################################
# roll_dice_on_thread()
###############################################

def roll_dice_on_thread(dice_strip, grid, rolling_dice):
    
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
    
    draw_grid(grid)
    rolling_dice = False

###############################################
# draw_grid()
###############################################

def draw_grid(grid):
    for col in range(COLS):
        for row in range(ROWS):
            draw_cell(grid, col, row)

###############################################
# draw_cell()
###############################################
            
def draw_cell(grid, col, row):
    x = GRID_LEFT + (CELL_HEIGHT * col)
    y = GRID_TOP + (CELL_WIDTH * row)
    
    if (grid[col, row] == CELL_BLOCKED):
        pygame.draw.ellipse(screen, TAN, (x + BORDER_SIZE, y + BORDER_SIZE, CELL_WIDTH - (2 * BORDER_SIZE), CELL_HEIGHT - (2 * BORDER_SIZE)))
    else:
        pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT))
        pygame.draw.rect(screen, CELL_COLORS[int(grid[col, row])], (x + BORDER_SIZE, y + BORDER_SIZE, CELL_WIDTH - (2 * BORDER_SIZE), CELL_HEIGHT - (2 * BORDER_SIZE)))

###############################################
# get_total_blockers()
###############################################

def get_total_blockers(grid):
    total = 0
    for col in range(COLS):
        for row in range(ROWS):            
            if (grid[col, row] == CELL_BLOCKED):
                total += 1
    return total


###############################################
# game_loop()
###############################################

def game_loop(grid, dice_strip, solved, solving, rolling_dice):
    game_exit = False
    clock = pygame.time.Clock()    

    while not game_exit:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) and (not (rolling_dice or solving)):
                game_exit = True;
            elif (event.type == pygame.MOUSEBUTTONDOWN) and (not (rolling_dice or solving)):
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if (roll_dice_label.is_over(mouse_x, mouse_y)):
                    roll_dice(grid, dice_strip, rolling_dice, solved)
                if (solve_label.is_over(mouse_x, mouse_y)):
                    solve(grid, solved, solving)
                if ((mouse_x > GRID_LEFT) and
                    (mouse_y > GRID_TOP) and
                    (mouse_x < GRID_LEFT + (COLS * CELL_WIDTH)) and
                    (mouse_y < GRID_TOP + (ROWS * CELL_HEIGHT))):
                    col = int((mouse_x - GRID_LEFT) // CELL_WIDTH)
                    row = int((mouse_y - GRID_TOP) // CELL_HEIGHT)
                    if (grid[col, row] == CELL_EMPTY):
                        total_blockers = get_total_blockers(grid)
                        if (total_blockers < TOTAL_DICE):
                            grid[col, row] = CELL_BLOCKED
                    elif (grid[col, row] == CELL_BLOCKED):
                        grid[col, row] = CELL_EMPTY
                    draw_cell(grid, col, row)

        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()

###############################################
# main()
###############################################

def main():
    pygame.init()
    
    # Strip for 7 dice
    dice_strip = np.ndarray(TOTAL_DICE, DiceCell)

    # Actual grid
    grid = np.zeros([COLS, ROWS])

    solving = False
    solved = False
    rolling_dice = False

    initialise(dice_strip, grid)

    draw_ui(dice_strip)
    roll_dice(grid, dice_strip, rolling_dice, solved)

    game_loop(grid, dice_strip, solved, solving, rolling_dice)

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()

