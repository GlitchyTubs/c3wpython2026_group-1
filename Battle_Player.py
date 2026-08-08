import pygame
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))



class Battle_Player(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()

            self.image = pygame.image.load("Solum_assets/BATTLE_PLAYER.png").convert_alpha()
            self.rect = self.image.get_rect()


            self.rect.x=50
            self.rect.y=500
            self.attack_speed = 100
           
        

    def move_attack(self, direction):
          keys_attack = pygame.key.get_pressed()
          if self.rect.y >= 500:
                  if keys_attack[pygame.K_DOWN]:
                  
                   self.rect.y-=self.attack_speed
          if self.rect.y <= 200:
                  if keys_attack[pygame.K_UP]:
                   self.rect.y+=self.attack_speed
          
          
          if keys_attack[pygame.K_UP]:
                    self.rect.y -= self.attack_speed
         
                               
          if keys_attack[pygame.K_DOWN]:
                    self.rect.y +=self.attack_speed

    






            

    