###############################################
# Main UI component sizes
###############################################

COLS = 6
ROWS = 6

CELL_WIDTH = 50
CELL_HEIGHT = CELL_WIDTH

TOTAL_DICE = 7

WINDOW_WIDTH = CELL_WIDTH * TOTAL_DICE

TOP_LABEL_WIDTH = WINDOW_WIDTH
TOP_LABEL_HEIGHT = CELL_HEIGHT

DICE_STRIP_WIDTH = WINDOW_WIDTH
DICE_STRIP_HEIGHT = CELL_HEIGHT

WINDOW_HEIGHT = TOP_LABEL_HEIGHT + DICE_STRIP_HEIGHT + (CELL_HEIGHT * (ROWS + 1))

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
CYAN = (0, 255, 255)

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

DICE_0_VALUES = [(0, 0), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5)]
DICE_1_VALUES = [(4, 0), (1, 5), (4, 0), (1, 5), (5, 1), (0, 4)]
DICE_2_VALUES = [(3, 0), (4, 1), (4, 2), (5, 2), (5, 3), (5, 5)]
DICE_3_VALUES = [(4, 5), (4, 4), (3, 5), (4, 3), (3, 4), (5, 4)]
DICE_4_VALUES = [(2, 2), (3, 2), (2, 3), (3, 1), (3, 3), (2, 4)]
DICE_5_VALUES = [(1, 1), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2)]
DICE_6_VALUES = [(0, 5), (5, 0), (5, 0), (5, 0), (0, 5), (0, 5)]

###############################################
# Label properties
###############################################

LABEL_BORDER_COLOR = WHITE
LABEL_COLOR = BLACK
LABEL_BORDER_SIZE = BORDER_SIZE
LABEL_FONT_COLOR = WHITE
LABEL_FONT_SIZE = FONT_SIZE

###############################################
# PyGame
###############################################

CLOCK_TICK = 30