import pygame
import random
import os
import sys
import Robot_Bomber
import Evade_Player
import Battle_Player
import Battle_Object
import Robot_Sword
import Sword_Slash
import Play_Combat
import Bombs


WIDTH= 720
HEIGHT= 720
FPS= 30
SLASH_EVENT = pygame.USEREVENT + 1
EXPLODE_EVENT= pygame.USEREVENT + 3
CHANGE_PHASE_EVENT = pygame.USEREVENT + 2
PHASE_DURATION = 5000
phase_change=1
phase_changed= False
enemy_health = random.randint(15,30)
player_health = 10
combat_button_clicked = False
phase_start_time = pygame.time.get_ticks()
# attack_mode= False
# player_turn= False

os.chdir(os.path.dirname(os.path.abspath(__file__)))






               

    



def slash():
                

                        if event.type == SLASH_EVENT:
                                sword_slash.rect.x=random.randint(10,720)
                                sword_slash.rect.y= random.randint(300,720)
                        if sword_slash.frame_index >= 3:
                                if evade_player.hit_timer == 0:
                                        if pygame.sprite.spritecollide(evade_player,sword_slash_group,False):
                                                global player_health
                                                player_health-=1
                                                evade_player.hit_timer= 15
                                        if phase_change == 1:
                                                evade_player.hit_timer = 100

                       



def explode():
                                 
                          
          
                                  if event.type == EXPLODE_EVENT:
                                          bomb.rect.x=random.randint(50,650)
                                          bomb.rect.y= random.randint(300,650)
                                  if bomb.frame_index >= 3:
                                          if evade_player.hit_timer == 0:
                                                  if pygame.sprite.spritecollide(evade_player,bomb_group,False):
                                                          global player_health
                                                          player_health-=1
                                                          evade_player.hit_timer= 15

                                                  if phase_change == 1:
                                                          evade_player.hit_timer = 25




                          


                                  






#Stages of Combat
def attack_phase():
            battle_line_1 = pygame.image.load("Solum_assets/battle_line.png").convert_alpha()
            battle_line_2 = pygame.image.load("Solum_assets/battle_line.png").convert_alpha()
            battle_line_3 = pygame.image.load("Solum_assets/battle_line.png").convert_alpha()
            battle_line_4 = pygame.image.load("Solum_assets/battle_line.png").convert_alpha()
            screen.fill((0,0,0))
            screen.blit(battle_line_1,(0,-130))
            screen.blit(battle_line_2,(0,-30))
            screen.blit(battle_line_3,(0,70))
            screen.blit(battle_line_4,(0,170))
            screen.blit(attack_player.image,attack_player.rect)
            battle_objects1_group.update()
            battle_objects2_group.update()
            battle_objects3_group.update()
            battle_objects4_group.update()
            battle_objects1_group.draw(screen)
            battle_objects2_group.draw(screen)
            battle_objects3_group.draw(screen)
            battle_objects4_group.draw(screen)


def sword_evade_phase():
            screen.fill((0,0,0))
            screen.blit(evade_player.image,evade_player.rect)
            robot_sword.update()
            screen.blit(robot_sword.image,robot_sword.rect)
            sword_slash_group.update()
            sword_slash_group.draw(screen)

def bomb_evade_phase():
            screen.fill((0,0,0))
            screen.blit(evade_player.image,evade_player.rect)
            robot_bomber.update()
            screen.blit(robot_bomber.image,robot_bomber.rect)
            bomb_group.update()
            bomb_group.draw(screen)


def neutral_phase_for_sword():
                screen.fill((0,0,0))
                screen.blit(robot_sword.image,robot_sword.rect)
                screen.blit(play_combat_button.image,play_combat_button.rect)

def neutral_phase_for_bomb():
                screen.fill((0,0,0))
                screen.blit(robot_bomber.image,robot_bomber.rect)
                screen.blit(play_combat_button.image,play_combat_button.rect)


                          

def health_display():
            player_health_text= pixel_font.render(f"Player Health: {player_health}", True, (255, 255, 255))
            enemy_health_text= pixel_font.render(f"Enemy Health: {enemy_health}", True, (255, 255, 255))
            screen.blit(player_health_text,(10,10))
            screen.blit(enemy_health_text,(10,50))



def detect_mouse_button():
                global phase_change
                global combat_button_clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                                  if play_combat_button.rect.collidepoint(mouse_pos):
                                          if not combat_button_clicked: 
                                            combat_button_clicked = True
                                            phase_change = 1
        
                                            pygame.time.set_timer(CHANGE_PHASE_EVENT, PHASE_DURATION)

def change_phase():
        global phase_change
        if event.type == CHANGE_PHASE_EVENT:
                        if phase_change==1:
                                phase_change=0
                        else:
                          phase_change=1
           
def display_phase_for_sword():
        global combat_button_clicked
        global phase_change
        if combat_button_clicked:
              
                      
                
        
                screen.fill((0,0,0))
                if phase_change==1:
                                attack_phase()
                                health_display()
                if phase_change==0:
                                sword_evade_phase()
                                health_display()
        else:
                           screen.fill((0,0,0))
                           neutral_phase_for_sword()
                           health_display()


def display_phase_for_bomb():
        global combat_button_clicked
        global phase_change
        if combat_button_clicked:
              
                      
                
        
                screen.fill((0,0,0))
                if phase_change==1:
                                attack_phase()
                                health_display()
                if phase_change==0:
                                bomb_evade_phase()
                                health_display()
        else:
                           screen.fill((0,0,0))
                           neutral_phase_for_bomb()
                           health_display()                              

def player_attack():
                global enemy_health
                if pygame.sprite.spritecollide(attack_player,battle_objects1_group,True) :
                            enemy_health-=1
                            for i in range(1):
                                                    battle_object1= Battle_Object.BO_1()
                                                    battle_objects1_group.add(battle_object1)
        
                if pygame.sprite.spritecollide(attack_player,battle_objects2_group,True) :
                                        enemy_health-=1
                                        for i in range(1):
                                                                battle_object2= Battle_Object.BO_2()
                                                                battle_objects2_group.add(battle_object2)
        
                if pygame.sprite.spritecollide(attack_player,battle_objects3_group,True) :
                                        enemy_health-=1
                                        for i in range(1):
                                                                battle_object3= Battle_Object.BO_3()
                                                                battle_objects3_group.add(battle_object3)
                if pygame.sprite.spritecollide(attack_player,battle_objects4_group,True) :
                                        enemy_health-=1
                                        for i in range(1):
                                                                battle_object4= Battle_Object.BO_4()
                                                                battle_objects4_group.add(battle_object4)


pygame.init()
pygame.mixer.init()
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solum")
clock = pygame.time.Clock()

pixel_font = pygame.font.Font("Solum_assets/Minecraft.ttf", 36)




attack_player= Battle_Player.Battle_Player()
evade_player= Evade_Player.Evade_Player()

battle_objects1_group= pygame.sprite.Group()
battle_object1= Battle_Object.BO_1()
battle_objects1_group.add(battle_object1)

battle_objects2_group= pygame.sprite.Group()
battle_object2= Battle_Object.BO_2()
battle_objects2_group.add(battle_object2)


battle_objects3_group= pygame.sprite.Group()
battle_object3= Battle_Object.BO_3()
battle_objects3_group.add(battle_object3)

battle_objects4_group= pygame.sprite.Group()
battle_object4= Battle_Object.BO_4()
battle_objects4_group.add(battle_object4)

robot_sword= Robot_Sword.Robot_Sword()
robot_bomber= Robot_Bomber.Robot_Bomber()
sword_slash_group= pygame.sprite.Group()
bomb_group = pygame.sprite.Group()
play_combat_button= Play_Combat.Play_Combat_Button()

for i in range(10):
    sword_slash= Sword_Slash.Sword_Slash()
    sword_slash_group.add(sword_slash)

for i in range(2):
        bomb=Bombs.Bombs()
        bomb_group.add(bomb)


pygame.time.set_timer(SLASH_EVENT,  2000,loops=0)
pygame.time.set_timer(EXPLODE_EVENT,  2000,loops=0)




running = True




while running:
    current_time = pygame.time.get_ticks()
    #Clock
    clock.tick(FPS)
    mouse_pos= pygame.mouse.get_pos()
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False

        detect_mouse_button()
       
        change_phase()
        
                                   
                                             
                                             

        if event.type == pygame.KEYDOWN:
                        keys_attack = pygame.key.get_pressed()
                        attack_player.move_attack(keys_attack) 

        for sword_slash in sword_slash_group:
                            slash()

        for bomb in bomb_group:
                            explode() 

    keys_evade = pygame.key.get_pressed()
    evade_player.move_evade(keys_evade)


    display_phase_for_bomb()
   
        
    
   
                                          
    
    
        
    evade_player.update_timer()
    player_attack()
    evade_player.boudaries() 
    
        
                       

    pygame.display.flip()
             
                 
    clock.tick(60)

pygame.quit()