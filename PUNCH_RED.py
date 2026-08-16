import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Robot_Punch_Red(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                
        
                rand_choices =[300,600,400,500]
                self.image = pygame.image.load("Solum_assets/RED_PUNCH_RIGHT.png").convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                
                self.rect = self.image.get_rect()
                
                self.rect.x= 700
                self.rect.y= random.choice(rand_choices)
                self.speed= random.randint(15,30)
        def update(self):
                  rand_choices =[300,600,400,500]
                  self.rect.x -= self.speed
                  
                                                  
                  if self.rect.x <= 0:
                                     
                                      
                        self.rect.y= random.choice(rand_choices)
                        self.rect.x= random.randint(750,900)
                        self.speed= random.randint(20,30) 