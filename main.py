#importing important tools
from os import system, name
from time import sleep
from random import randrange
import random
import pygame

#pygame setup
pygame.init()
screenwidth = 500
screenheight = 500
win = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Tile-Based RPG")

#important variables
game = True
run = True
boxXpos = []
boxYpos = []
boxXsize = []
boxYsize = []
position = 0

#character info
x = 250
y = 250
width = 40
height = 40
vel = 5
character = pygame.draw.rect(win, (46, 204, 113), (x,  y, width, height))

#creates a class of obstacles with assigned info
class obstacle:
    def __init__(self, name, xPos, yPos, xSize, ySize):
        self.name = name
        self.xPos = xPos
        self.yPos = yPos
        self.xSize = xSize
        self.ySize = ySize

    #draws rectangles with the objects from the class, if cut is true it creates a blank spot in the wall
    def drawObstacle(self, cut=False):
        if cut == False:
            self.name = pygame.draw.rect(win, (250,0,0), (self.xPos, self.yPos, self.xSize, self.ySize))
        if cut == True:
            self.name = pygame.draw.rect(win, (250,0,0), (self.xPos, self.yPos, self.xSize, self.ySize))
            if self.xPos == 0 and self.yPos == 0 and self.xSize == 20:
                pygame.draw.rect(win, (0,0,0), (0, 200, 20, 100))
            if self.xPos == 480 and self.yPos == 0:
                pygame.draw.rect(win, (0,0,0), (480, 200, 20, 100))
            if self.xPos == 0 and self.yPos == 0 and self.xSize == 500:
                pygame.draw.rect(win, (0,0,0), (200, 0, 100, 20))
            if self.xPos == 0 and self.yPos == 480:
                pygame.draw.rect(win, (0,0,0), (200, 480, 100, 20))
            
#goals - creates room with: walls, random boxes in the middle   
def createroom():
    global boxNum
    global boxXpos
    global boxYpos
    global boxXsize
    global boxYsize
    global leave

    #randomises where exit will be
    leave = position
    while leave == position:
        leave = randrange(4)

    #create boxes
    boxXpos.clear()
    boxYpos.clear()
    boxNum = randrange(4)
    for i in range(boxNum + 3):
        boxXpos.append(random.randint(60, 365))
        boxYpos.append(random.randint(60, 365))
        boxXsize.append(random.randint(50, 75))
        boxYsize.append(random.randint(50, 75))

#draws room every movement
def drawroom():
    global leftWall
    global rightWall
    global upWall
    global downWall
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6

    #draw walls
    if leave == 0:
        leftWall = obstacle("leftWall", 0, 0, 20, 500)
        leftWall.drawObstacle(True)
        rightWall = obstacle("rightWall", 480, 0, 20, 500)
        rightWall.drawObstacle()
        upWall = obstacle("upWall", 0, 0, 500, 20)
        upWall.drawObstacle()
        downWall = obstacle("downWall", 0, 480, 500, 20)
        downWall.drawObstacle()
    elif leave == 1:
        rightWall = obstacle("rightWall", 480, 0, 20, 500)
        rightWall.drawObstacle(True)
        upWall = obstacle("upWall", 0, 0, 500, 20)
        upWall.drawObstacle()
        downWall = obstacle("downWall", 0, 480, 500, 20)
        downWall.drawObstacle()
        leftWall = obstacle("leftWall", 0, 0, 20, 500)
        leftWall.drawObstacle()
    elif leave == 2:
        upWall = obstacle("upWall", 0, 0, 500, 20)
        upWall.drawObstacle(True)
        downWall = obstacle("downWall", 0, 480, 500, 20)
        downWall.drawObstacle()
        leftWall = obstacle("leftWall", 0, 0, 20, 500)
        leftWall.drawObstacle()
        rightWall = obstacle("rightWall", 480, 0, 20, 500)
        rightWall.drawObstacle()
    elif leave == 3:
        downWall = obstacle("downWall", 0, 480, 500, 20)
        downWall.drawObstacle(True)
        leftWall = obstacle("leftWall", 0, 0, 20, 500)
        leftWall.drawObstacle()
        rightWall = obstacle("rightWall", 480, 0, 20, 500)
        rightWall.drawObstacle()
        upWall = obstacle("upWall", 0, 0, 500, 20)
        upWall.drawObstacle()

    #better way to draw
    # for l in boxYpos:
    #     l += 1
    #     draw rect with info from lists

    #draw boxes
    box1 = obstacle("box1", boxXpos[0], boxYpos[0], boxXsize[0], boxYsize[0])
    box1.drawObstacle()
    box2 = obstacle("box2", boxXpos[1], boxYpos[1], boxXsize[1], boxYsize[1])
    box2.drawObstacle()
    if boxNum == 0:
        box3 = obstacle("box3", boxXpos[2], boxYpos[2], boxXsize[2], boxYsize[2])
        box3.drawObstacle()
    if boxNum >= 1:
        box4 = obstacle("box4", boxXpos[3], boxYpos[3], boxXsize[3], boxYsize[3])
        box4.drawObstacle()
    if boxNum >= 2:
        box5 = obstacle("box5", boxXpos[4], boxYpos[4], boxXsize[4], boxYsize[4])
        box5.drawObstacle()
    if boxNum >= 3:
        box6 = obstacle("box6", boxXpos[5], boxYpos[5], boxXsize[5], boxYsize[5])
        box6.drawObstacle()

#run game
while run == True:
    #updates/creates a new room with new obstacles
    createroom()
    game = True

    #looks at input
    while game == True:
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                pygame.font.quit()
                quit()
        
        keys = pygame.key.get_pressed()

        counter = -1
        for l in boxXpos:
            counter += 1

            if character.colliderect(box1) == False and character.colliderect(box2) == False and character.colliderect(box3) == False and character.colliderect(box4) == False and character.colliderect(box5) == False and character.colliderect(box6) == False:
            #if x + vel <= boxXpos[counter] or x + vel >= boxXpos[counter] + boxXsize[counter] and y >= boxYpos[counter] and y <= boxYpos[counter] + boxYsize[counter]:
                if keys[pygame.K_RIGHT]and x + 20 <= screenwidth - width - vel:
                    x += vel

            #if x - vel >= boxXpos[counter] + boxXsize[counter] or x - vel <= boxXpos[counter] and y >= boxYpos[counter] and y <= boxYpos[counter] + boxYsize[counter]:
                if keys[pygame.K_LEFT] and x - 20 >= vel:
                    x -= vel

            #if y + vel != boxYpos[counter] + boxYsize[counter] and y <= boxXpos[counter] and y  >= boxXpos[counter] + boxXsize[counter]:
                if keys[pygame.K_DOWN] and y + 20 <= screenheight - height - vel:
                    y += vel

            #if y - vel != boxYpos[counter] and y <= boxXpos[counter] and y >= boxXpos[counter] + boxXsize[counter]:
                if keys[pygame.K_UP] and y - 20 >= vel:
                    y -= vel

        #checks if player goes into exit
        if leave == 0 and x == 20 and y >= 200 and y <= 300:
            x = 480 - width
            y = 270
            position = 0
            game = False
        if leave == 1 and x == 480 - width and y >= 200 and y <= 300:
            x = 20
            y = 270
            position = 1
            game = False
        if leave == 2 and x >= 200 and x <= 300 and y == 20:
            x = 230
            y = 480 - height
            position = 2
            game = False
        if leave == 3 and x >= 200 and x <= 300 and y == 480 - height:
            x = 230
            y = 20
            position = 3
            game = False

        win.fill((0,0,0))
        drawroom()
        character = pygame.draw.rect(win, (46, 204, 113), (x,  y, width, height))   
        pygame.display.update() 


