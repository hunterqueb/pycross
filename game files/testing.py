import random
import math

from win32api import *
from picross_functions import *
# a=1
# i=0
# while i in range(5):
#     print(i)
#     i = i + 1
#     if i == 2:
#         i=4

# import pygame
#
# WINDOW_SIZE_SIDE = 255
# WINDOW_SIZE = [WINDOW_SIZE_SIDE, WINDOW_SIZE_SIDE]
# WIDTH = WINDOW_SIZE[0]/12.75
#
# print(WIDTH)
# print(random.randint(int(0.36*10*10),int(0.52*10*10)))
#
# print(math.ceil(5/2))
savedindex=[None,None]
array = init_array(5)
# guess_array = init_guess_array(5)
# guess_in_array(guess_array,0,0)
# print(guess_array)

rown = get_row_numbers(array,5)
