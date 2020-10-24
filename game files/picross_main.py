#PYTHON PICROSS
#HOW?
#
#load gui
#	get a size (right now do 5x5)
#       OPTIONS
#           autostrike-out row after fully populating row
#

#custom functions
from picross_functions import *

#import pygame for WINDOW
import pygame
import random
import math
# import win32api for display settings
from win32api import *

# How Big is the Array?
gameSize = 5

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKGREY = (34, 34, 34)

# Get the width of the monitor divide by 2 and set a square window size
WINDOW_SIZE_SIDE=int(GetSystemMetrics(0)/2)
WINDOW_SIZE = [WINDOW_SIZE_SIDE, WINDOW_SIZE_SIDE]

# get the display device used and get the refreshRate
device = EnumDisplayDevices()
settings = EnumDisplaySettings(device.DeviceName, -1)
refreshRate = getattr(settings, 'DisplayFrequency')

# This sets the WIDTH and HEIGHT of each grid location along with a fixed margin - consider changing this
MARGIN = 5
WIDTH = (WINDOW_SIZE_SIDE - MARGIN * (gameSize+2))/(gameSize+1)
HEIGHT = WIDTH

#initialize the grid array used for coloring picross ui
grid = []
for row in range(gameSize+1):
    grid.append([])
    for column in range(gameSize+1):
        grid[row].append(0)  # Append a cell

# pre pygame window calculations
#initialize arrays for storing game
gameArray=init_array(gameSize)
guessArray=init_guess_array(gameSize)

#initialze the hints for the user
rowHints = get_row_numbers(gameArray,gameSize)
columnHints = get_column_numbers(gameArray,gameSize)

# Initialize pygame
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Picross")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            try:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = int((pos[0]-(WIDTH + MARGIN)) // (WIDTH + MARGIN))
                row = int((pos[1]-(HEIGHT + MARGIN)) // (HEIGHT + MARGIN))

                # prevent game from crashing if you click outside of array
                if column > gameSize-1 or row > gameSize-1:
                    break
                # dont allow clicking in boxes used for numbers
                if column < 0 or row < 0:
                    break

                # checks to see if what previous direction the player was moving and fixes all guessing to that direction
                if lastDir == 'row':
                    row = savedIndex[0]
                elif lastDir == 'column':
                    column = savedIndex[1]

                # prevents rapid guessing as mouse movements are updated
                if lastArrayAccess == [row,column]:
                    break

            # Toggle location and set state depending on mouse click
                # Empty cell and left click
                if grid[row+1][column+1] == 0 and pygame.mouse.get_pressed()[0] > 0:
                    grid[row+1][column+1] = 1
                    guess_in_array(guessArray,row,column)
                # guessed cell and left click
                elif grid[row+1][column+1] == 1 and pygame.mouse.get_pressed()[0] > 0:
                    grid[row+1][column+1] = 0
                    rm_guess_in_array(guessArray,row,column)
                # empty cell and right clicked
                elif grid[row+1][column+1] == 0 and pygame.mouse.get_pressed()[2] > 0:
                    grid[row+1][column+1] = 2
                # blocked cell and right clicked
                elif grid[row+1][column+1] == 2 and pygame.mouse.get_pressed()[2] > 0:
                    grid[row+1][column+1] = 0
                    rm_guess_in_array(guessArray,row,column)
                # guessed cell and right clicked
                elif grid[row+1][column+1] == 1 and pygame.mouse.get_pressed()[2] > 0:
                    grid[row+1][column+1] = 0
                    rm_guess_in_array(guessArray,row,column)

                # saves the index of the array to prevent to be used above to force guessing in only one direction per mouse click
                if savedIndex[0] == row:
                    lastDir = 'row'
                elif savedIndex[1] == column:
                    lastDir = 'column'
                else: # in the even that that it is your first movement, save the index
                    savedIndex=[row,column]

                # prevents messed up behavior when holding down Lclick
                lastArrayAccess = [row,column]

                # debug print
                print("Click ", pos, "Grid coordinates: ", row, column)

            except AttributeError:
                pass
        else:
            lastArrayAccess = [-2,-2]
            lastDir = None
            savedIndex=[None,None]
    # Set the screen background
    screen.fill(DARKGREY)

    # Draw the grid
    for row in range(gameSize+1):
        for column in range(gameSize+1):
            color = WHITE
            #for left click draw green
            if grid[row][column] == 1:
                color = GREEN
            #for right click draw red
            elif grid[row][column] == 2:
                color = RED
            #draw rectangles on screen
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Turn on VSYNC
    clock.tick(refreshRate)

    # update the screen
    pygame.display.flip()


pygame.quit()



# NOTES

# 1 screen with to choose size
# 1 screen that will be used to play the game
# 1 screen that shows you win and replay the game

if gameArray==guessArray:
    #draw a win condition
    print('You Win!!!!!!')
    # draw something that will change the screen
    #click to restart?
