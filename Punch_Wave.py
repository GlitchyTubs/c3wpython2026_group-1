import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys




os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Punch_Wave(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
                
                self.image = pygame.image.load("Solum_assets/punch_wave1.png").convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect()
                self.rect.x= 650
                self.rect.y= 300
                self.speed = random.randint(10,15)

                
                        

        def update(self):
          

            if self.rect.x <= -600:
                                   
                                            
                                            self.rect.y= 300
                                            self.rect.x= 720
                                            self.speed= random.randint(10,15)
            self.animate()
        
        def animate(self):
                
                  self.rect.x -= self.speed
                  

        