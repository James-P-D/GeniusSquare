import pygame
from Constants import *

class DiceCell():
    __x = 0
    __y = 0
    __width = 0
    __height = 0
    __value = 0
    __possible_values = []

    def __init__(self, x, y, width, height, possible_values):
        self.__x = int(x)
        self.__y = int(y)
        self.__width = int(width)
        self.__height = int(height)
        self.__value = 0
        self.__possible_values = possible_values

    def draw(self, screen):        
        pygame.draw.rect(screen, DICE_CELL_BORDER_COLOR, (self.__x, self.__y, self.__width, self.__height), 0)        
        pygame.draw.rect(screen, DICE_CELL_COLOR, (self.__x + DICE_CELL_BORDER_SIZE, self.__y + DICE_CELL_BORDER_SIZE, self.__width - (DICE_CELL_BORDER_SIZE * 2), self.__height - (DICE_CELL_BORDER_SIZE * 2)), 0)

        if (self.__value != -1):
            label_font = pygame.font.SysFont('courier', DICE_CELL_FONT_SIZE, bold = True)
            label_text = label_font.render(str(self.get_label()), 1, DICE_CELL_FONT_COLOR)
            label_x = ((self.__width / 2) - (label_text.get_width() / 2) + self.__x)
            label_y = ((self.__height / 2) - (label_text.get_height() / 2) + self.__y)
            screen.blit(label_text, (int(label_x), int(label_y)))

    def is_over(self, mouse_x, mouse_y):
        return ((mouse_x >= self.__x) and (mouse_x < (self.__x + self.__width)) and (mouse_y >= self.__y) and (mouse_y < (self.__y + self.__height)))
        
    def inc_value(self):
        self.__value = (self.__value + 1) % (len(self.__possible_values))

    def get_value(self):
        return self.__possible_values[self.__value]

    def get_label(self):
        (col, row) = self.get_value()
        return DICE_ROW_IDS[row] + DICE_COLUMN_IDS[col]