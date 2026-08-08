import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))





class Bombs(pygame.sprite.Sprite):
          def __init__(self):
                         super().__init__()
         
                         self.frames =[
         
                                               
                                               pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(), 
                                               pygame.image.load("Solum_assets/bombs1.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs2.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs3.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs4.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs5.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs6.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs7.png").convert_alpha(),
                                               pygame.image.load("Solum_assets/bombs8.png").convert_alpha()
                                               
                                               ]
                 
                         self.frame_index=0
                         
                         self.animation_speed=0.49
                         
                         
                         
                         self.image = pygame.image.load("Solum_assets/sword_warning.png").convert_alpha()
                         self.rect = self.image.get_rect()
         
                         self.rect.x= random.randint(10,600)
                         self.rect.y= random.randint(300,600)
          def update(self):
                         self.animate()
                         
                         
                           
                         
                 
          def animate(self):
                           self.frame_index+= self.animation_speed
                           if self.frame_index > len(self.frames):
                             self.frame_index=0
                           self.image=self.frames[int(self.frame_index)]