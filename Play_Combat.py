import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys




class Play_Combat_Button(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
   
                self.image = pygame.image.load("Solum_assets/PLAY_COMBAT.png").convert_alpha()
                self.image= pygame.transform.scale(self.image,(400,200))
                self.rect = self.image.get_rect()
                self.rect.x= 150
                self.rect.y= 400