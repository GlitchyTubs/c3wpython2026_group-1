import pygame
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Evade_Player(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()

            self.image = pygame.image.load("Solum_assets/BATTLE_PLAYER.png").convert_alpha()
            self.rect = self.image.get_rect()


            self.rect.x=20
            self.rect.y=400
            self.evade_speed = 20
            self.hit_timer= 0

    def boudaries(self): 
                 self.rect.x = max(0, min(self.rect.x, WIDTH - 50))
                 self.rect.y = max(300, min(self.rect.y, HEIGHT - 100))

    def move_evade(self, direction):
         
          keys_evade = pygame.key.get_pressed()
          if keys_evade[pygame.K_UP]:
                    self.rect.y -= self.evade_speed
         
                               
          if keys_evade[pygame.K_DOWN]:
                    self.rect.y +=self.evade_speed

          if keys_evade[pygame.K_LEFT]:
                        self.rect.x -= self.evade_speed

          if keys_evade[pygame.K_RIGHT]:
                        self.rect.x += self.evade_speed

    def update_timer(self):
                if self.hit_timer > 0:
                    self.hit_timer -= 1