import pygame
WIDTH= 720
HEIGHT= 720
import os
import sys
import random
import Main_Game

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ENEMY_DICT= {
                1:pygame.image.load("Solum_assets/robot_sword_floor.png").convert_alpha(),
                2:pygame.image.load("Solum_assets/robot_run_floor.png").convert_alpha(),
                3:pygame.image.load("Solum_assets/robot_laser_floor.png").convert_alpha(),
                4:pygame.image.load("Solum_assets/robot_bomber_floor.png").convert_alpha(),
                5:pygame.image.load("Solum_assets/floor_punch.png").convert_alpha()
            }



class Floor_Enemy(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()

            
            self.image = pygame.image.load("Solum_assets/floor_punch.png").convert_alpha()
            self.rect = self.image.get_rect()
            

            self.rect.x=300
            self.rect.y=360
            
            self.rand_enemies=ENEMY_DICT
            
            self.rand_enemy= random.randint(1,5)
            self.image= self.rand_enemies[self.rand_enemy]

    
    def change_enemy(self):
       
        self.rand_enemy= random.randint(1,5)
        self.image= self.rand_enemies[self.rand_enemy]
        

                
    

    
    