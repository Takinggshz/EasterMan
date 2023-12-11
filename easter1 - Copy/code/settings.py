import pygame 



vec = pygame.math.Vector2
Height = 800
Width = 1550

Acc = 1
Friction = -0.1 #CHANGE THIS DEPENDING ON TERRAIN
Jump_height = 100 #Jump height y value
Fps = 60
Fps_Clock = pygame.time.Clock()

displaysurf = pygame.display.set_mode((Width,Height))
tilesize = 64