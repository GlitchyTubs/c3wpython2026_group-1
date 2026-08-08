import pygame
import os
import sys


os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Robot_Bomber(pygame.sprite.Sprite):
            def __init__(self):
                    super().__init__()
    
                    self.frames =[
                                          pygame.image.load("Solum_assets/robot_bomb1.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb2.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb3.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb4.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb5.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb6.png").convert_alpha(),
                                          pygame.image.load("Solum_assets/robot_bomb7.png").convert_alpha(),
                                          ]
            
                    self.frame_index=0
                    self.animation_speed=0.2
                    self.image = pygame.image.load("Solum_assets/robot_bomb1.png").convert_alpha()
                    self.image= pygame.transform.scale(self.image,(300,300))
                    
                    self.rect = self.image.get_rect()
                    self.rect.x= 240
                    self.rect.y= 20
            def update(self):
                      self.animate()
            
            def animate(self):
                      self.frame_index+= self.animation_speed
                      if self.frame_index > len(self.frames):
                        self.frame_index=0
                      self.image=self.frames[int(self.frame_index)]