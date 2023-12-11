#Submission to easter pygame gamejam
#__Authors__ = VishyBoi(RocktheRock), Takinggshz(itch.io name here)
#v 1.0.0
#Creative commons license

#!!!! TODO - Music, complete the levels, beginning and end screen, saving high score/level, player attack


import pygame,sys
from pygame.locals import *
from map import map_1
import csv
from settings import displaysurf,Fps,Fps_Clock,Height
from level import Level
from player import Player

pygame.init()


Name = "DragonEgg"

pygame.display.set_caption(Name)
pygame.mixer.init()
#give some sound here

class background:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.img = pygame.image.load('code/pics/bgs/bg_1.png')
    def draw(self):
         self.show =  displaysurf.blit(self.img,(self.x,self.y))

     
  




        




bg = background(0,0)
level = Level(map_1 ,displaysurf)
run = True
 
#Rendering the image as per the level
#!!!! CHANGE FRICTION DEPENDING UPON 

while run:
    displaysurf.fill((0,0,0))
    level.run()
  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE: 
                run = False

        if event.type == pygame.QUIT:
            run = False
       
      
    
    #displaysurf.blit(player.image,player.rect)
    pygame.display.update()
    Fps_Clock.tick(Fps)
