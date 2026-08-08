import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))





class Sword_Slash(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                self.frames =[

                                      
                                      pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword_warning.png").convert_alpha(), 
                                      pygame.image.load("Solum_assets/sword1v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword2v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword2v3.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword4v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword5v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword6v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword7v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword8v2.png").convert_alpha(),
                                      pygame.image.load("Solum_assets/sword9v2.png").convert_alpha(),
                                      ]
        
                self.frame_index=0
                
                self.animation_speed=0.49
                
                
                
                self.image = pygame.image.load("Solum_assets/sword1v2.png").convert_alpha()
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