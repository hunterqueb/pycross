#PYTHON PICROSS
#HOW?
#
#load gui
#	get a size (right now do 5x5)
#       OPTIONS
#           autostrike-out row after fully populating row
#


#import pygame for WINDOW
import math
import time
import pygame


#custom functions
import picross_functions
import colors
# import win32api for display settings
import win32api


# MAIN GAME LOGIC


# How Big is the Array?
gameSize = 5
groupNum = math.ceil(gameSize/2)


arial = picross_functions.search_font('arial')

# Get the width of the monitor divide by 2 and set a square window size
WINDOW_SIZE_SIDE = int(win32api.GetSystemMetrics(0)/2)
WINDOW_SIZE = [WINDOW_SIZE_SIDE, WINDOW_SIZE_SIDE]

# get the display device used and get the refreshRate
device = win32api.EnumDisplayDevices()
settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
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
gameArray = picross_functions.init_true_rand_array(gameSize)
guessArray = picross_functions.init_guess_array(gameSize)

#initialze the hints for the user
print(gameArray)
rowHints = picross_functions.get_row_numbers(gameArray, gameSize)
columnHints = picross_functions.get_column_numbers(gameArray,gameSize)

print(rowHints)
print(columnHints)

transposedColumnHints = []
transposedColumnHints = picross_functions.transpose(
    columnHints, transposedColumnHints)


# Initialize pygame
pygame.init()

screenGame = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

# Set title of screen
pygame.display.set_caption("Picross")

# Loop until the user clicks the close button.
done = False
winCondtion = 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.VIDEORESIZE:
            screenGame = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
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
                    picross_functions.guess_in_array(guessArray,row-groupNum,column-groupNum)
                # guessed cell and left click
                elif grid[row-groupNum][column-groupNum] == 1 and pygame.mouse.get_pressed()[0] > 0:
                    #prevent user from doubling back on there guess choice if held down
                    grid[row-groupNum][column-groupNum] = 0
                    picross_functions.rm_guess_in_array(guessArray,row-groupNum,column-groupNum)
                # empty cell and right clicked
                elif grid[row-groupNum][column-groupNum] == 0 and pygame.mouse.get_pressed()[2] > 0:

                    grid[row-groupNum][column-groupNum] = 2

                # blocked cell and right clicked
                elif grid[row-groupNum][column-groupNum] == 2 and pygame.mouse.get_pressed()[2] > 0:
                    #prevent user from doubling back on there remove choice if held down
                    grid[row-groupNum][column-groupNum] = 0
                    picross_functions.rm_guess_in_array(guessArray,row-groupNum,column-groupNum)


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
    screenGame.fill(colors.DARKGREY)

    # Draw the grid

    for row in range(gameSize+groupNum):
        for column in range(gameSize+groupNum):
            color = colors.WHITE
            #for left click draw green
            if grid[row-groupNum][column-groupNum] == 1:
                color = colors.GREEN
            #for right click draw red
            elif grid[row-groupNum][column-groupNum] == 2:
                color = colors.RED
            # dont draw the squares in the upper right corner that goes unused
            if row < groupNum and column < groupNum:
                continue
            #draw rectangles on screen
            pygame.draw.rect(screenGame, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            
            # draw the row hints
            if column < groupNum:
                picross_functions.message_display(arial, int(HEIGHT), colors.BLACK, ((WIDTH/2)+(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row), str(rowHints[row-groupNum][column]), screenGame)
            else:
                pass
            
    # draw the column hints
    for column in range(gameSize+groupNum):
        for row in range(gameSize+groupNum):
            if column >= groupNum and row < groupNum:
                picross_functions.message_display(arial,int(HEIGHT),colors.BLACK,((WIDTH/2)+(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row),str(transposedColumnHints[row][column-groupNum]),screenGame)
            else:
                pass

    # Turn on VSYNC
    clock.tick(refreshRate)

    if gameArray == guessArray:
        done = True
        winCondtion = 1
    # update the screenGame
    pygame.display.flip()
    
#draw a win condition
if winCondtion == 1:
    screenGame.fill(colors.DARKGREY)
    winFontSize = 200
    otherFont = 100
    arial = picross_functions.search_font('arial')
    picross_functions.message_display(arial, winFontSize, colors.WHITE, (WINDOW_SIZE_SIDE-850, WINDOW_SIZE_SIDE-650), "YOU WIN",screenGame)
    picross_functions.message_display(arial, otherFont, colors.WHITE, (WINDOW_SIZE_SIDE-850+50, WINDOW_SIZE_SIDE-650+winFontSize), "Closing in 5 sec...",screenGame)
    pygame.display.flip()
    time.sleep(5)
    #click to restart?

pygame.quit()



# NOTES

# 1 screen with to choose size
# 1 screen that will be used to play the game
# 1 screen that shows you win and replay the game
