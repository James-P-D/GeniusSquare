###############################################
# Main UI component sizes
###############################################

COLS = 6
ROWS = 6

CELL_WIDTH = 50
CELL_HEIGHT = CELL_WIDTH

TOTAL_DICE = 7

WINDOW_WIDTH = CELL_WIDTH * TOTAL_DICE

ROLL_DICE_LABEL_WIDTH = WINDOW_WIDTH
ROLL_DICE_LABEL_HEIGHT = CELL_HEIGHT

DICE_STRIP_TOP = ROLL_DICE_LABEL_HEIGHT
DICE_STRIP_WIDTH = WINDOW_WIDTH
DICE_STRIP_HEIGHT = CELL_HEIGHT

COL_LABEL_STRIP_TOP = DICE_STRIP_TOP + CELL_HEIGHT

SOLVE_LABEL_TOP = COL_LABEL_STRIP_TOP + CELL_HEIGHT + (ROWS * CELL_HEIGHT)
SOLVE_LABEL_WIDTH = WINDOW_WIDTH
SOLVE_LABEL_HEIGHT = CELL_HEIGHT

GRID_TOP = ROLL_DICE_LABEL_HEIGHT + DICE_STRIP_HEIGHT + CELL_HEIGHT
GRID_LEFT = CELL_WIDTH

WINDOW_HEIGHT = ROLL_DICE_LABEL_HEIGHT + DICE_STRIP_HEIGHT + CELL_HEIGHT + (CELL_HEIGHT * ROWS ) + SOLVE_LABEL_HEIGHT

FONT_SIZE = 20
BORDER_SIZE = 2

###############################################
# RGB Colors
###############################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (210, 105, 30)
ORANGE = (255, 165, 0)
DARK_GRAY = (140, 140, 140)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
TAN = (220, 202, 152)

###############################################
# Dice properties
###############################################

DICE_COLUMN_IDS = "123456"
DICE_ROW_IDS = "ABCDEF"

DICE_CELL_BORDER_COLOR = BLACK
DICE_CELL_COLOR = WHITE
DICE_CELL_BORDER_SIZE = BORDER_SIZE
DICE_CELL_FONT_COLOR = BLACK
DICE_CELL_FONT_SIZE = FONT_SIZE

# Dice values
DICE_VALUES = [[(0, 0), (0, 2), (0, 3), (1, 3), (1, 4), (2, 5)],
               [(4, 0), (1, 5), (4, 0), (1, 5), (5, 1), (0, 4)],
               [(3, 0), (4, 1), (4, 2), (5, 2), (5, 3), (5, 5)],
               [(4, 5), (4, 4), (3, 5), (4, 3), (3, 4), (5, 4)],
               [(2, 2), (3, 2), (2, 3), (3, 1), (3, 3), (2, 4)],
               [(1, 1), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2)],
               [(0, 5), (5, 0), (5, 0), (5, 0), (0, 5), (0, 5)]]

###############################################
# Label properties
###############################################

LABEL_BORDER_COLOR = WHITE
LABEL_COLOR = BLACK
LABEL_BORDER_SIZE = BORDER_SIZE
LABEL_FONT_COLOR = WHITE
LABEL_FONT_SIZE = FONT_SIZE

###############################################
# Cell types
###############################################

CELL_COLORS = [BLACK,       # Empty cell
               BLUE,        # Single-cell blue piece
               BROWN,       # Double-cell brown piece
               ORANGE,      # Straight triple-cell orange piece
               PURPLE,      # Corner triple-cell purple piece
               DARK_GRAY,   # Staight four-cell gray piece
               RED,         # Zig-zag four-cell red piece
               YELLOW,      # T-shape four-cell yellow piece
               CYAN,        # L-shape four-cell cyan piece
               GREEN]       # Green four-cell square

CELL_BLOCKED = -1
CELL_EMPTY = 0

# Single-cell blue piece
CELL_TYPE_1 = [[[1]]]       

# Double-cell brown piece
CELL_TYPE_2 = [[[2],
                [2]],

               [[2, 2]]]

# Straight triple-cell orange piece
CELL_TYPE_3 = [[[3],
                [3],
                [3]],
               
               [[3, 3, 3]]]

# Corner triple-cell purple piece
CELL_TYPE_4 = [[[4, 4],
                [4, 0]],

               [[4, 4],
                [0, 4]],

               [[4, 0],
                [4, 4]],

               [[0, 4],
                [4, 4]]]

# Staight four-cell gray piece
CELL_TYPE_5 = [[[5],
                [5],
                [5],
                [5]],

               [[5, 5, 5, 5]]]

# Zig-zag four-cell red piece
CELL_TYPE_6 = [[[0, 6, 6],
                [6, 6, 0]],
               
               [[6, 6, 0],
                [0, 6, 6]],

               [[6, 0],
                [6, 6],
                [0, 6]],

               [[0, 6],
                [6, 6],
                [6, 0]]]

# T-shape four-cell yellow piece
CELL_TYPE_7 = [[[7, 0],
                [7, 7],
                [7, 0]],

               [[0, 7],
                [7, 7],
                [0, 7]],

               [[7, 7, 7],
                [0, 7, 0]],

               [[0, 7, 0],
                [7, 7, 7]]] 

# L-shape four-cell cyan piece
CELL_TYPE_8 = [[[8, 0],
                [8, 0],
                [8, 8]],

               [[0, 8],
                [0, 8],
                [8, 8]],

               [[8, 8],
                [8, 0],
                [8, 0]],

               [[8, 8],
                [0, 8],
                [0, 8]],

               [[8, 8, 8],
                [8, 0, 0]],

               [[8, 8, 8],
                [0, 0, 8]],

               [[8, 0, 0],
                [8, 8, 8]],

               [[0, 0, 8],
                [8, 8, 8]]]

# Green four-cell square
CELL_TYPE_9 = [[[9, 9],
                [9, 9]]]

# All the pieces in ascending order of size
PIECE_SHAPES = [CELL_TYPE_1,
                CELL_TYPE_2,
                CELL_TYPE_3,
                CELL_TYPE_4,
                CELL_TYPE_5,
                CELL_TYPE_6,
                CELL_TYPE_7,
                CELL_TYPE_8,
                CELL_TYPE_9]

###############################################
# PyGame
###############################################

CLOCK_TICK = 30
SLEEP_DELAY = 0.01