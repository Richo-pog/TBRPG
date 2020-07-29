#importing important tools
from os import system, name
from time import sleep
from random import randrange
import pygame
pygame.init()

screenwidth = 500
screenheight = 500
win = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Tile-Based RPG")
game = True
x = 225
y = 225
width = 50
height = 50
vel = 5

while game == True:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            pygame.font.quit()
            quit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel

    if keys[pygame.K_RIGHT]and x <= screenwidth - width - vel:
        x += vel

    if keys[pygame.K_UP] and y >= vel:
        y -= vel

    if keys[pygame.K_DOWN] and y <= screenheight - height - vel:
        y += vel

    win.fill((0,0,0))  
    pygame.draw.rect(win, (250,0,0), (x,  y, width, height))   
    pygame.display.update() 
    
 

