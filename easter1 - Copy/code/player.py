import pygame
from settings import displaysurf,Height,Width
from folder import import_folder



class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        
        self.facing_right = True
        self.speed = 5     
        self.jump_height = 39
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = .15
        self.status = 'Idle'
        self.g = 3
        self.shi = False
        self.direction = pygame.math.Vector2(0,0)
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.on_ground = False
        self.on_ceil = False
        self.on_left = False
        self.on_right = False
        self.Jump_speed = self.jump_height
        self.friction = 0.6

       
    def import_character_assets(self):
        character_path = 'code/pics/player/'
        self.animations = {'Idle':[],'Jump':[],'Run':[],'Attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    def animate(self):

        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.facing_right == True:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
        
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        
        if self.on_ceil and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceil and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceil:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
    def move(self):

        keyispressed = pygame.key.get_pressed()

        if keyispressed[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False        
        elif keyispressed[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0     

        if keyispressed[pygame.K_SPACE] and self.on_ground: 

    
                self.jump()
        if keyispressed[pygame.K_LCTRL or pygame.K_RCTRL]:
            self.crouch()
        if keyispressed[pygame.K_UP]:
            self.shi = True
        else:
            self.shi = False
            

    def get_status(self):
        if self.on_ground == False:
            self.status  = 'Jump'
        else:
           
            if self.direction.x != 0:
                self.status = 'Run'
            
            else:
                self.status = 'Idle'

                if self.shi == True:
                    self.status = 'Attack'
                
    
    def gravity(self):
        self.direction.y += self.g
        self.rect.y += self.direction.y
       
    def jump(self):
         self.direction.y -= self.Jump_speed
         self.Jump_speed -= self.g
        
         if self.direction.y <= (Height - self.jump_height):
            self.Jump_speed  = self.jump_height
            
            self.on_ground = False
    def crouch(self):
        
        if self.direction.x == -1:
            self.direction.x += self.friction

        elif self.direction.x == 1:
            self.direction.x -= self.friction
        
        else:
            self.direction.x = self.direction.x

    
    def confirmation(self):
        if self.on_left == True:
            print('L')
        elif self.on_right == True:
            print('R')

    def draw(self):
        
        self.blit = displaysurf.blit(self.image, (self.rect.x,self.rect.y))
             

    def update(self):
        self.get_status()
        self.draw()
        self.animate()
        self.confirmation()
        self.move()
       
     
        

