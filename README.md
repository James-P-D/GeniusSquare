# Genius Square
Genius Square puzzle solver in Python

![Screenshot](https://github.com/James-P-D/GeniusSquare/blob/master/screenshot.gif)

## Introduction

[The Genius Square](https://www.happypuzzle.co.uk/products/genius-square.aspx) is a spacial awareness game for children. The game consists of seven, six-sided dice, a `6x6` board, 7 'blocker' pieces, and 9 tetris-like pieces of different shapes.

A player rolls seven six-sided dice:

![Dice](https://github.com/James-P-D/GeniusSquare/blob/master/dice.jpg)

Each dice is then used to put a 'blocker' piece on the board at the given location:

![Initial Board](https://github.com/James-P-D/GeniusSquare/blob/master/initial_board.jpg)

The player then takes the 9 coloured pieces and attempts to fit them onto the board:

![Pieces](https://github.com/James-P-D/GeniusSquare/blob/master/pieces.jpg)

One completed state for the board would be as follows:

![Completed Board](https://github.com/James-P-D/GeniusSquare/blob/master/completed_board.jpg)

## Algorithm

To solve the puzzle we take one of the largest pieces, in our case the four-cell-square piece and attempt to find a place on the board where it fits in. Once we have done so, we then check the next smallest piece and attempt to find a place where that also fits. At some point we will reach a situation where there are no locations where the current piece can go. At this point we back-track to the previous pieces and see if there are additional locations that can be used. This is continued until we reach the smallest piece, which should fit in the large remaining cell.

## Usage

Simply click <kbd>ROLL DICE</kbd> to set the seven blocker cells. Then click <kbd>SOLVE</kbd> to solve the puzzle.

Alternatively, after rolling the dice, you can toggle the location of blocker peices. Note however that by manually choosing the location of blocker peices, it is possible to create unsolveable puzzles such as the one below:

![Screenshot](https://github.com/James-P-D/GeniusSquare/blob/master/unsolvable.gif)

After ~8 minutes of running, the game will produce a message in the console stating `No Solution Found!`.

## Setup

For Python we need the following:

[pygame](https://www.pygame.org/news) (Tested with v1.9.6)  
[numpy](https://numpy.org/) (Tested with v1.18.3)  

```
pip install pygame
pip install numpy
```