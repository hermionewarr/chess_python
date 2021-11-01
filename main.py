# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:39:16 2021

@author: hermi
"""

#import board
#import pieces

import pygame
import sys
import time


game_over = False 
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while not game_over:
    
    screen.fill(black)
    pygame.display.flip()
    
    game_over = True
    