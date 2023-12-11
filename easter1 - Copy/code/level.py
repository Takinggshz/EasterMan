import pygame
from map import map_1
from support import import_csv_function,import_cut_graphics
from blocks import Tile,Statictile
from settings import tilesize
from player import Player

class Level:
    def __init__(self,map_data,surface):
        
        self.display_surface = surface
        self.world_shift = -2
        terrain_layout = import_csv_function(map_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')
        coin_layout =  import_csv_function(map_data['coin'])
        self.coin_sprites = self.create_tile_group(coin_layout,'coin') 
        self.player = Player((400,0))
        self.current_x = 0
      
    def create_tile_group(self,layout,type):
        
        
      
        self.sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * tilesize   
                    y = row_index * tilesize
                    x_smol = col_index * 32
                    y_smol = row  * 32

                    if type == 'terrain':

                        terrain_tile_list = import_cut_graphics('code/pics/tiles/terrain.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = Statictile(tilesize,x,y,tile_surface)
                        self.sprite_group.add(sprite)

                    if type == 'coin':

                        coin_tile_list = import_cut_graphics('code/pics/tiles/coin.png')
                        coin_tile_surface = coin_tile_list[int(val)]
                        coin_sprite = Statictile(tilesize,x,y,coin_tile_surface)
                        self.sprite_group.add(coin_sprite)
                
        

        return self.sprite_group  
    def scroll_x(self):
        player = self.player
        
        player_x = player.rect.x
        direction_x = player.direction.x

        if player_x < 388 and direction_x < 0:
            self.world_shift = 10
            player.speed = 0
        elif player_x > 1164 and direction_x > 0:
            self.world_shift = -10
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 10   
        
    def horizontal_movement_and_collision(self):
     player = self.player
     player.rect.x += player.direction.x * player.speed
     
     for sprite in self.terrain_sprites.sprites():
         if sprite.rect.colliderect(player.rect):
             if player.direction.x < 0:
                 player.on_left = True
                 player.rect.left = sprite.rect.right
                 self.current_x = player.rect.left
             elif player.direction.x > 0:
                 player.on_right = True
                 player.rect.right = sprite.rect.left
                 self.current_x = player.rect.right
     
     if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
         player.on_left = False
     if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
         player.on_right = False

    def vertical_movement_and_collision(self):
        player = self.player
        player.gravity()

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceil = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceil and player.direction.y > 0:
            player.on_ceil = False
       
    
    def run(self):
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)
        self.coin_sprites.update(self.world_shift)
        self.player.update()
        self.scroll_x()
        self.horizontal_movement_and_collision()
        self.vertical_movement_and_collision()
    