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

def message_display(used_font, size, color,xy,message):
    font_object = pygame.font.Font(used_font, size)
    rendered_text = font_object.render(message, True, (color))
    screenGame.blit(rendered_text,(xy))

def search_font(name):
    found_font = pygame.font.match_font(name)
    return found_font

# How Big is the Array?
gameSize = 5
groupNum=math.ceil(gameSize/2)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKGREY = (34, 34, 34)

arial = search_font('arial')

# Get the width of the monitor divide by 2 and set a square window size
WINDOW_SIZE_SIDE=int(GetSystemMetrics(0)/2)
WINDOW_SIZE = [WINDOW_SIZE_SIDE, WINDOW_SIZE_SIDE]

# get the display device used and get the refreshRate
device = EnumDisplayDevices()
settings = EnumDisplaySettings(device.DeviceName, -1)
refreshRate = getattr(settings, 'DisplayFrequency')

# This sets the WIDTH and HEIGHT of each grid location along with a fixed margin - consider changing this
MARGIN = 5
WIDTH = (WINDOW_SIZE_SIDE - MARGIN * (gameSize+2*groupNum))/(gameSize+1*groupNum)
HEIGHT = WIDTH

#initialize the grid array used for coloring picross ui
grid = []
for row in range(gameSize+groupNum):
    grid.append([])
    for column in range(gameSize+groupNum):
        grid[row].append(0)  # Append a cell

# pre pygame window calculations
#initialize arrays for storing game
gameArray=init_array(gameSize)
guessArray=init_guess_array(gameSize)

#initialze the hints for the user
print(gameArray)
rowHints = get_row_numbers(gameArray,gameSize)
columnHints = get_column_numbers(gameArray,gameSize)
print(rowHints)
print(columnHints)

# Initialize pygame
pygame.init()

screenGame = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Picross")
# text = font.render('GeeksForGeeks', True, BLACK, WHITE)


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
                column = int((pos[0]-(WIDTH + MARGIN)) // (WIDTH + MARGIN)) + 1
                row = int((pos[1]-(HEIGHT + MARGIN)) // (HEIGHT + MARGIN)) + 1
                # prevent game from crashing if you click outside of array
                if column > gameSize+groupNum-1 or row > gameSize+groupNum-1:
                    break
                # dont allow clicking in boxes used for numbers
                if column < groupNum or row < groupNum:
                    break

                # checks to see if what previous direction the player was moving and fixes all guessing to that direction
                if lastDir == 'row':
                    row = savedIndex[0]
                elif lastDir == 'column':
                    column = savedIndex[1]

                # prevents rapid guessing as mouse movements are updated
                if [row,column] == lastArrayAccess:
                    break

                # if lastDir == 'row' or lastDir == 'column':
                #     break
            # Toggle location and set state depending on mouse click
                # Empty cell and left click
                if grid[row-groupNum][column-groupNum] == 0 and pygame.mouse.get_pressed()[0] > 0:
                    grid[row-groupNum][column-groupNum] = 1
                    guess_in_array(guessArray,row-groupNum,column-groupNum)
                # guessed cell and left click
                elif grid[row-groupNum][column-groupNum] == 1 and pygame.mouse.get_pressed()[0] > 0:
                    #prevent user from doubling back on there guess choice if held down
                    grid[row-groupNum][column-groupNum] = 0
                    rm_guess_in_array(guessArray,row-groupNum,column-groupNum)
                # empty cell and right clicked
                elif grid[row-groupNum][column-groupNum] == 0 and pygame.mouse.get_pressed()[2] > 0:

                    grid[row-groupNum][column-groupNum] = 2

                # blocked cell and right clicked
                elif grid[row-groupNum][column-groupNum] == 2 and pygame.mouse.get_pressed()[2] > 0:
                    #prevent user from doubling back on there remove choice if held down
                    grid[row-groupNum][column-groupNum] = 0
                    rm_guess_in_array(guessArray,row-groupNum,column-groupNum)


                # saves the index of the array to be used above to force guessing in only one direction per mouse click
                if savedIndex[0] == row:
                    lastDir = 'row'
                elif savedIndex[1] == column:
                    lastDir = 'column'
                else: # in the event that that it is your first movement, save the index
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
    screenGame.fill(DARKGREY)

    # Draw the grid
    for row in range(gameSize+groupNum):
        for column in range(gameSize+groupNum):
            color = WHITE
            #for left click draw green
            if grid[row-groupNum][column-groupNum] == 1:
                color = GREEN
            #for right click draw red
            elif grid[row-groupNum][column-groupNum] == 2:
                color = RED
            # dont draw the squares in the upper right corner that goes unused
            if row < groupNum and column < groupNum:
                continue
            #draw rectangles on screen
            pygame.draw.rect(screenGame, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

            message_display(arial,int(HEIGHT),BLACK,((MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row),str(1))
    # for row in range(gameSize+groupNum):
    #     for column in range(gameSize+groupNum):

    # Turn on VSYNC
    clock.tick(refreshRate)

    # update the screenGame
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
