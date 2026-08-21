from Main_Game import start_game
import pygame
import Screen
import Battle_Object

current_floor = 1

get_enemy_health = start_game().get("enemy_health")


def Entrance(): 
    def __init(self, x, y, width, height, text, color):
        self.x = 750 
        self.y = 250
        self.width = 350
        self.height = 150
        self.color = (255, 255, 255)

for _ in range(4):
    if int(Battle_Object.BO_1) <= 0 and int(Battle_Object.BO_2) <= 0 and int(Battle_Object.BO_3) <= 0 and int(Battle_Object.BO_4) <= 0:
        pygame.draw.rect(Screen, (100, 70, 350, 150), Entrance())
        if Battle_Object.rect.colliderect(Entrance()):
            current_floor += 1
        if current_floor == 5:
            break
        
