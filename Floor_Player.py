import pygame
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Floor_Player(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()

            self.frames =[
                                                      
                                                      pygame.image.load("Solum_assets/Floor_Player_Walk1.png").convert_alpha(),
                                                      pygame.image.load("Solum_assets/Floor_Player_Walk1.png").convert_alpha(),
            ]
            self.reversed_frames= []

            for frame in self.frames:
                    self.reversed_frame=pygame.transform.flip(frame,True,False)
                    self.reversed_frames.append(self.reversed_frame)
            self.image = pygame.image.load("Solum_assets/Floor_Player_Walk1.png").convert_alpha()
            self.rect = self.image.get_rect()
            

            self.rect.x=300
            self.rect.y=50
            self.frame_index=0
            self.animation_speed=0.2
            self.evade_speed = 10
            self.hit_timer= 0
            self.moving=False
            self.reversed_moving=False

    def boudaries(self): 
                 self.rect.x = max(0, min(self.rect.x, WIDTH - 50))
                 self.rect.y = max(0, min(self.rect.y, HEIGHT - 100))

    def move_floor(self, keys):
          self.moving= False
          self.reversed_moving=False
         
          keys= pygame.key.get_pressed()
          if keys[pygame.K_UP]:
                    self.rect.y -= self.evade_speed
                    self.moving=True
         
                               
          if keys[pygame.K_DOWN]:
                    self.rect.y +=self.evade_speed
                    self.moving=True

          if keys[pygame.K_LEFT]:
                        self.rect.x -= self.evade_speed
                        self.moving=False
                        self.reversed_moving=True

          if keys[pygame.K_RIGHT]:
                        self.rect.x += self.evade_speed
                        self.moving=True
                        self.reversed_moving=False

    def update(self):
                    if self.moving:
                          self.animate()
                    if self.reversed_moving:
                            self.reversed_animate()


                
    def animate(self):
                          self.frame_index+= self.animation_speed
                          if self.frame_index >= len(self.frames):
                            self.frame_index=0
                          self.image=self.frames[int(self.frame_index)]
    def reversed_animate(self):
                              self.frame_index+= self.animation_speed
                              if self.frame_index >= len(self.frames):
                                self.frame_index=0
                              self.image=self.reversed_frames[int(self.frame_index)]

    
    