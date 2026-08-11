import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Laser_Beam(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                self.frames =[        
                                      pygame.image.load("Solum_assets/laser_beam1.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/laser_beam2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/laser_beam3.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/laser_beam4.png").convert_alpha(),
                                     
                                      ]
        
                self.frame_index=0
                self.animation_speed=0.2
                self.image = pygame.image.load("Solum_assets/laser_beam4.png").convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x= 650
                self.rect.y= random.randint(300,690)
                self.speed = random.randint(30,50)
        def update(self):
                  self.animate()
        
        def animate(self):
                
                  self.rect.x -= self.speed
                  
                  self.frame_index+= self.animation_speed
                  if self.frame_index > len(self.frames):
                    self.frame_index=0
                  self.image=self.frames[int(self.frame_index)]
                               
                  if self.rect.x <= 0:
                            self.rect.y= random.randint(300,690)
                            self.rect.x= random.randint(750,900)
                            self.speed= random.randint(30,50)

        