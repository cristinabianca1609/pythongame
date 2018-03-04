#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:56:03 2018

@author: cristina
"""

# 1. Import library
import pygame
from pygame.locals import *

#2. Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]

#3. Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

#4.  Keep looping through
while 1:
    #5. Clear the screen before drawing it again
    screen.fill(0)
    #6. Draw the screen elements
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100, y*100))
    screen.blit(castle,(0, 30))
    screen.blit(castle,(0, 135))
    screen.blit(castle,(0, 240))
    screen.blit(castle,(0, 345))
    screen.blit(player, (100, 100))
    #7. Update the screen
    pygame.display.flip()
    #8. Loop through the events
    for event in pygame.event.get():
        # check if the event is the x button
        if event.type == pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
    

