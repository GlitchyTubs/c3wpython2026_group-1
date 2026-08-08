import pygame
import random
WIDTH= 720
HEIGHT= 720
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))






class BO_1(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
   
                self.image = pygame.image.load("Solum_assets/BATTLE_OBJECT.png").convert_alpha()
                self.image= pygame.transform.scale(self.image,(50,50))
                self.rect = self.image.get_rect()
                self.rect.x= random.randint(750,900)
                self.rect.y= 500
                self.speed = random.randint(20,30)

        def update(self):
                       
            self.rect.x -= self.speed
                                
            if self.rect.x <= 0:
                   
                    
                            self.rect.y= 500
                            self.rect.x= random.randint(750,900)
                            self.speed= random.randint(20,30)                        

class BO_2(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
   
                self.image = pygame.image.load("Solum_assets/BATTLE_OBJECT.png").convert_alpha()
                self.image= pygame.transform.scale(self.image,(50,50))
                self.rect = self.image.get_rect()
                self.rect.x= random.randint(750,900)
                self.rect.y= 400
                self.speed = random.randint(20,30)

        def update(self):
                     
            self.rect.x -= self.speed
                                
            if self.rect.x <= 0:
                    self.rect.y= 400
                    self.rect.x= random.randint(750,900)
                    self.speed= random.randint(20,30)
       
class BO_3(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
   
                self.image = pygame.image.load("Solum_assets/BATTLE_OBJECT.png").convert_alpha()
                self.image= pygame.transform.scale(self.image,(50,50))
                self.rect = self.image.get_rect()
                self.rect.x= random.randint(750,900)
                self.rect.y= 300
                self.speed = random.randint(20,30)

        def update(self):
                     
            self.rect.x -= self.speed
                                
            if self.rect.x <= 0:
                   
                    
                            self.rect.y= 300
                            self.rect.x= random.randint(750,900)
                            self.speed= random.randint(20,30)

class BO_4(pygame.sprite.Sprite):
        def __init__(self):
                super().__init__()
        
   
                self.image = pygame.image.load("Solum_assets/BATTLE_OBJECT.png").convert_alpha()
                self.image= pygame.transform.scale(self.image,(50,50))
                self.rect = self.image.get_rect()
                self.rect.x= random.randint(750,900)
                self.rect.y= 200
                self.speed = random.randint(20,30)

        def update(self):
                     
            self.rect.x -= self.speed
                                
            if self.rect.x <= 0:
                   
                    
                            self.rect.y= 200
                            self.rect.x= random.randint(750,900)
                            self.speed= random.randint(20,30)
