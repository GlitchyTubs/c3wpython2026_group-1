import Battle_Player
import pygame

current_floor = 1
entrance = pygame.Rect(750, 250, 40, 100)
pygame.draw.rect(screen, (100, 70, 40), entrance)

if Battle_Player.colliderect(entrance):
    current_floor += 1
    Battle_Player.x = 50
    Battle_Player.y = 300

if current_floor == 1:
    entrance = pygame.Rect(750, 250, 40, 100)

elif current_floor == 2:
    entrance = pygame.Rect(750, 250, 40, 100)

elif current_floor == 3:
    entrance = pygame.Rect(750, 250, 40, 100)

elif current_floor == 4:
    entrance = pygame.Rect(750, 250, 40, 100)

elif current_floor == 5:
    pass