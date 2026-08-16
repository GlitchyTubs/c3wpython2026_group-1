import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Robot_Punch_Blue(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                
        
                

                self.image = pygame.image.load("Solum_assets/BLUE_PUNCH_LEFT.png").convert_alpha()
                self.rect = self.image.get_rect()
                self.speed= random.randint(15,30)
        def update(self):
                  self.rect.x -= self.speed
                  
                                                  
                  if self.rect.x <= 300:
                                                       
                                                        
                        self.rect.y= 400
                        self.rect.x= random.randint(750,900)
                        self.speed= random.randint(20,30) 