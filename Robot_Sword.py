import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Robot_Sword(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                self.frames =[
                                      pygame.image.load("Solum_assets/Robot_swing_1.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/Robot_swing_2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/Robot_swing_3.png").convert_alpha()
                                      ]
        
                self.frame_index=0
                self.animation_speed=0.2
                self.image = pygame.image.load("Solum_assets/Robot_swing_1.png").convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.x= 250
                self.rect.y= -5
        def update(self):
                  self.animate()
        
        def animate(self):
                  self.frame_index+= self.animation_speed
                  if self.frame_index > len(self.frames):
                    self.frame_index=0
                  self.image=self.frames[int(self.frame_index)]