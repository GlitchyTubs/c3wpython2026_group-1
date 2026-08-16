import pygame
import Evade_Player
import Main_Game
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Player_Shield(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()

                self.image = pygame.image.load("Solum_assets/BLUE_PUNCH_LEFT.png").convert_alpha()
                self.rect = self.image.get_rect()
                

                self.rect.x= 360
                self.rect.y=400
                self.speed = 20

        def update(self):
            self.rect.x+= self.speed