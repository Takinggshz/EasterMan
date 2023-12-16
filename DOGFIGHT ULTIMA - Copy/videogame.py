import pygame
import math
import random
from pygame import mixer

pygame.init()
pygame.display.set_caption("Dog Fight Ultimate")
screen = pygame.display.set_mode((800,500))
rock = pygame.image.load('rock.png')
pygame.display.set_icon(rock)

bg = pygame.image.load('bg.png')
mixer.music.load('bgm.wav')
mixer.music.play(-1)
score_value = 0
font = pygame.font.SysFont('freesanbold.ttf',32)
end_font = pygame.font.SysFont('freesanbold.ttf',64)
textX = 10
textY = 10

#player
playerImg = pygame.image.load('player.png')
playerX = 330
playerY = 430

playerX_change = 0
#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 80)
enemyX_change = 0.3
enemyY_change = 0.06


#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 1
bullet_state = 'ready'



    
def player(x,y):
    screen.blit(playerImg, (x, y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+48, y+0))
def enemy(x,y):
    screen.blit(enemyImg,(x, y))
def fcollision(enemyX,enemyY,bulletX,bulletY):

#this meth to find distance between two coordinates
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
def sus_score(x,y):
    score = font.render("Score:  " +  str(score_value),True,(0,0,0))
    screen.blit(score, (x,y))
def game_over():
    over_text = font.render("GAME OVER",True,(0,0,0))
    over_text.blit(over_text, (200,250))
# loop
running = True
while running:
    
    screen.fill((0, 0, 0))
    screen.blit(bg,(0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    enemyY += enemyY_change

    #key control
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.9
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.9
        if bullet_state == 'ready':
            if event.key == pygame.K_UP:
                 shot_sound = mixer.Sound('shot.wav')
                 shot_sound.play()
                 bulletX = playerX
                 fire_bullet(bulletX,bulletY)

           
          
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    
    playerX += playerX_change
    enemyX += enemyX_change
    
    #rgb selection
    
    if playerX <= 0:
        playerX = 0
    elif playerX >=672:
        playerX = 672
    
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
    if enemyY > 500:
        break
        
        
        
    
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    #collison
    collision = fcollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        collision_sound = mixer.Sound('collision.wav')
        collision_sound.play()
        bulletY = 480
        bullet_state = 'ready'
        enemyX = random.randint(0, 736)
        enemyY = random.randint(0, 80)
        score_value += 1
        

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    sus_score(textX,textY)


    pygame.display.update()
    


