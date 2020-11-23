import random
import math
import pygame


def init_rand_array(n):
    #seed random generation
    random.SystemRandom()

    #initialize array and fill with all zeros
    array = [[0 for i in range(n)] for j in range(n)]

    #range 36 to 52% of the squares in an array should be filled
    squares = random.randint(int(0.36*n*n), int(0.52*n*n))

    fillCount = 0
    for i in range(n):
        for j in range(n):
            fill = random.randint(0, 1)
            if fillCount == squares:
                break
            if fill == 1:
                array[i][j] = 1
                fillCount += 1
            else:
                continue

    # print(array)
    return array

def init_true_rand_array(n):
    #seed random generation
    random.SystemRandom()

    #initialize array and fill with all zeros
    array = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            fill = random.randint(0, 1)
            if fill == 1:
                array[i][j] = 1
            else:
                continue

    # print(array)
    return array

def init_guess_array(n):

    #initialize array and fill with all zeros
    guess_array = [ [ 0 for i in range(n) ] for j in range(n) ]
    # print(guess_array)
    return guess_array

def guess_in_array(array,i,j):
    # changes value in guess array to 1 for a user guessed
    # array is passed by reference
    array[i][j] = 1
    # print(array)
    return

def rm_guess_in_array(array,i,j):
    # changes value in guess array from 1 to 0 for a user
    # array passed by reference
    array[i][j] = 0
    # print(array)
    return

def get_row_numbers(array,n):
    #largest group of numbers in a picross game as a function of the puzzle size
    groupNum=math.ceil(n/2)
    #initialize array
    row_numbers = [ [ 0 for i in range(groupNum) ] for j in range(n) ]
    j=0
    i=0
    k=0
    numCount=0

    while j in range(n): # iterate through rows
        while i in range(n): # iterate through the columns
            if array[j][i] == 1:
                k = i
                while k in range(n):
                    if array[j][k] == 0:
                        numRow = k-i
                        row_numbers[j][numCount] = numRow
                        numCount = numCount+1
                        i = k
                        break
                    elif k == n-1:
                        if k == i:
                            numRow = 1
                        else:
                            numRow = k-i+1
                        row_numbers[j][numCount] = numRow
                        numCount = numCount+1
                        i = k
                        break
                    k = k + 1
            i = i + 1
        j = j + 1
        i=0
        numCount = 0
    # print(row_numbers)
    return row_numbers


def get_column_numbers(array,n):
    #largest group of numbers in a picross game as a function of the puzzle size
    groupNum=math.ceil(n/2)
    #initialize array
    column_numbers = [ [ 0 for i in range(groupNum) ] for j in range(n) ]
    j=0
    i=0
    k=0
    numCount=0

    while i in range(n): # iterate through rows
        while j in range(n): # iterate through the columns
            if array[j][i] == 1:
                k = j
                while k in range(n):
                    if array[k][i] == 0:
                        numCol = k-j
                        column_numbers[i][numCount] = numCol
                        numCount = numCount+1
                        j = k
                        break
                    elif k == n-1:
                        if k == j:
                            numCol = 1
                        else:
                            numCol = k-j+1
                        column_numbers[i][numCount] = numCol
                        numCount = numCount+1
                        j = k
                        break
                    k = k + 1
            j = j + 1
        i = i + 1
        j=0
        numCount = 0
    # print(column_numbers)
    return column_numbers

def transpose(l1, l2):
    # for use in transposing the column hint array to easily display on screen the hints
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


def message_display(used_font, size, color, xy, message, screenGame):
    font_object = pygame.font.Font(used_font, size)
    rendered_text = font_object.render(message, True, (color))
    screenGame.blit(rendered_text, (xy))


def search_font(name):
    found_font = pygame.font.match_font(name)
    return found_font
