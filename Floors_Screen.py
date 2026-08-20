import pygame
WIDTH= 720
HEIGHT= 720
import os
import sys
import Main_Game
import Floor_Enemy
import Floor_Player

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode((720, 720))
floor_number=1
Main_Game.player_health=15
def Floors():
    background_image = pygame.image.load("Solum_assets/SFloors_Back.jpeg").convert()
    background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    screen.blit(background,(0,0))
    screen.blit(rand_enemy.image,(360,360))
    screen.blit(floor_player.image,(200,200))

def Floor_Change_Player():
    global floor_number
    if Main_Game.player_health <=0:
        if floor_number == 1:
            floor_number=1
        else:
         floor_number-=1
        
def Floor_Change_Enemy():
    global floor_number
    if Main_Game.enemy_health <=0:
                floor_number+=1


def Enemy_Collision():
    if rand_enemy.rand_enemy==1:
               if pygame.sprite.collide_rect(floor_player, rand_enemy):
                   Main_Game.start_game().display_phase_for_sword()
               
    elif rand_enemy.rand_enemy==2:
               self.image = pygame.image.load("Solum_assets/robot_run_floor.png").convert_alpha()
     
    elif rand_enemy.rand_enemy==3:
               self.image = pygame.image.load("Solum_assets/robot_laser_floor.png").convert_alpha()
     
    elif rand_enemy.rand_enemy==4:
               rand_enemy.image = pygame.image.load("Solum_assets/robot_bomber_floor.png").convert_alpha()
               



rand_enemy= Floor_Enemy.Floor_Enemy()
floor_player= Floor_Player.Floor_Player()