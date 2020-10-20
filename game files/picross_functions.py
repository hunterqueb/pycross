import random
import math

def init_array(n):
    #seed random generation
    random.SystemRandom()

    #initialize array and fill with all zeros
    array = [[0] * n for i in range(n)]

    #range 36 to 52% of the squares in an array should be filled
    squares = random.randint(int(0.36*n*n),int(0.52*n*n))

    fillCount = 0
    for i in range(n):
        for j in range(n):
            fill = random.randint(0,1)
            if fillCount == squares:
                break
            if fill == 1:
                array[i][j] = 1
                fillCount += 1
            else:
                continue

    print(array)
    return array

def init_guess_array(n):

    #initialize array and fill with all zeros
    guess_array = [[0] * n for i in range(n)]
    print(guess_array)
    return guess_array

def guess_in_array(array,i,j):
    # changes value in guess array to 1 for a user guessed
    # array is passed by reference
    array[i][j] = 1
    print(array)
    return

def rm_guess_in_array(array,i,j):
    # changes value in guess array from 1 to 0 for a user
    # array passed by reference
    array[i][j] = 0
    print(array)
    return

def get_row_numbers(array,n):
    #largest group of numbers in a picross game as a function of the puzzle size
    groupNum=math.ceil(n/2)
    #initialize array
    row_numbers = [[0] * groupNum] * n
    counti=0
    j=0
    i=0
    numCount=0

    while j in range(n):
        while i in range(n):
            if array[i][j] == 1:
                numBegin=i
                k=numBegin
                while array[k][j] == 1:
                    if array[k][j] == 0:
                        numEnd = k
                        num=numEnd-numBegin
                        row_numbers[numCount][j] = num
                        numCount = numCount + 1
                        i = numEnd
                        break
                    k=k+1
            else:
                i=i+1
        j = j + 1

    print(row_numbers)
    return row_numbers

def get_columns_numbers(array,n):


    return
