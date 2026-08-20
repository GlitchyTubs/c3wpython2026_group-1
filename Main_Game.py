
       



def start_game():
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
        import Robot_Runner
        import Robot_Run
        import Robot_Laser
        import Laser_Beam
        import Punch_Impact
        import Robot_Punch
        import Punch_Wave
        import Player_Shield
        import PUNCH_RED
        import Floor_Enemy
        import Floor_Player



         

        WIDTH= 720
        HEIGHT= 720
        FPS= 30
        SLASH_EVENT = pygame.USEREVENT + 1
        EXPLODE_EVENT= pygame.USEREVENT + 3
        PUNCH_EVENT=pygame.USEREVENT+4
        SWITCH_WAVES= pygame.USEREVENT +5
        SWITCH_PUNCH= pygame.USEREVENT +6
        CHANGE_PHASE_EVENT = pygame.USEREVENT + 2
        PHASE_DURATION = 5000
        phase_change=1
        punch_phase_change=1
        active_shield= False
        enemy_health = random.randint(15,30)
        player_health = 15
        floor_number=1
        game_state="Floor"
        combat_button_clicked = False
        phase_start_time = pygame.time.get_ticks()
        # attack_mode= False
        # player_turn= False

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        screen = pygame.display.set_mode((720, 720))
        clock= pygame.time.Clock()

        background_image = pygame.image.load("Solum_assets/Floors_Back.jpeg").convert()
        background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        win_image= pygame.image.load("Solum_assets/WIN_SCREEN.png").convert()
        win_screen= pygame.transform.scale(win_image, (WIDTH, HEIGHT))


        def Floors():
                
                screen.blit(background,(0,0))
                screen.blit(rand_enemy.image,rand_enemy.rect)
                floor_player.update()
                screen.blit(floor_player.image,floor_player.rect)

        def Floor_Change_Player():
                nonlocal floor_number
                nonlocal player_health
                nonlocal game_state
                if player_health <=0 and floor_number==1:
                        game_state="Floor"
                        floor_player.rect.x= 200
                        floor_player.rect.y= 200
                        floor_number=1
                        player_health=15
                        rand_enemy.change_enemy()
                               
                        pygame.display.flip()
                if player_health <=0 and floor_number >1: 
                                game_state="Floor"  
                                floor_player.rect.x= 200
                                floor_player.rect.y= 200   
                                floor_number-=1
                                player_health=15
                                rand_enemy.change_enemy()
                                
                                pygame.display.flip()
               
                        
                        
        
        def Floor_Change_Enemy():
                nonlocal enemy_health
                nonlocal player_health
                nonlocal floor_number
                nonlocal game_state
                if enemy_health <=0:
                        game_state="Floor"
                        floor_player.rect.x= 300
                        floor_player.rect.y= 50
                        floor_number+=1
                        enemy_health = random.randint(15,30)
                        player_health=15
                        rand_enemy.change_enemy()
                        
                        pygame.display.flip()

        def Enemy_Collision():
                nonlocal game_state
                if pygame.sprite.collide_rect(floor_player, rand_enemy):
                        game_state="Game"
                        if rand_enemy.rand_enemy==1:
                        
                                display_phase_for_sword()
               
                        elif rand_enemy.rand_enemy==2:
                        
                                display_phase_for_run()
     
                        elif rand_enemy.rand_enemy==3:
                        
                                display_phase_for_laser()
     
                        elif rand_enemy.rand_enemy==4:
                        
                                display_phase_for_bomb()
                        elif rand_enemy.rand_enemy==5:
                        
                                display_phase_for_punch()



        rand_enemy= Floor_Enemy.Floor_Enemy()
        floor_player= Floor_Player.Floor_Player()




        def game_win():
                nonlocal floor_number
                if floor_number > 5:
                        screen.blit(win_screen,(0,0))



        
        def i_frames():
                if phase_change == 1:
                        evade_player.hit_timer = 25  




        def is_shield_active():
                nonlocal active_shield
                if active_shield:
                        player_shield.update()
                        if player_shield.rect.x > 720:
                                active_shield = False

                else:
                        player_shield.rect.x = -1000
        
        def shield_follow(event):
                
                nonlocal active_shield
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                                if not active_shield:
                                        active_shield=True
                                        player_shield.rect.center = evade_player.rect.center
                                        
                                
                        
        def shield_collision():
                nonlocal player_health
                nonlocal active_shield
                if active_shield:
                  if pygame.sprite.spritecollide(player_shield,punch_group,True):
                                
                        
                                active_shield=False
                                player_shield.rect.x+=-1000
                                for i in range (1):
                                                punch_red=PUNCH_RED.Robot_Punch_Red()
                                                punch_group.add(punch_red)
                if evade_player.hit_timer == 0:
                 if pygame.sprite.spritecollide(evade_player, punch_group, True, pygame.sprite.collide_mask):
                                                
                    player_health-=1
                    evade_player.hit_timer= 15
                    
                           
                    for i in range (1):
                        punch_red=PUNCH_RED.Robot_Punch_Red()
                        punch_group.add(punch_red)

        
        def change_punch_impact_and_waves():
                nonlocal phase_change
                nonlocal punch_phase_change
                if event.type == CHANGE_PHASE_EVENT and phase_change ==0:
                        evade_player.rect.x = 10
                        evade_player.rect.y = 500

                        if punch_phase_change==1:
                                        punch_phase_change=0
                        else:
                                        punch_phase_change=1



        def punch_impact_and_waves():
                if punch_phase_change==1:
                                punch_impact_evade_phase()
                                punch_wave.rect.x+=-1000
                                        
                if punch_phase_change==0:
                                punch_wave_evade_phase()
                                        
               



               

    
        def run_collision():
                 nonlocal player_health
                 if evade_player.hit_timer == 0:
                     if pygame.sprite.spritecollide(evade_player, run_group, False, pygame.sprite.collide_mask):
                                                 player_health
                                                 player_health-=1
                                                 evade_player.hit_timer= 5
                                                 


        def punch_wave_collision():
                 nonlocal player_health
                 if event.type == SWITCH_WAVES and phase_change == 1:
                                     rand_wave=random.randint(1,4)
                                     if rand_wave == 1:
                                       punch_wave.image= pygame.image.load("Solum_assets/punch_wave1.png").convert_alpha()
                                     elif rand_wave ==2:
                                      punch_wave.image = pygame.image.load("Solum_assets/punch_wave2.png").convert_alpha()
                                     elif rand_wave == 3:
                                      punch_wave.image = pygame.image.load("Solum_assets/punch_wave3.png").convert_alpha()
                 if evade_player.hit_timer == 0:
                    
                   
                               
                    if pygame.sprite.collide_mask(evade_player, punch_wave):

                                                 player_health-=1
                                                 evade_player.hit_timer= 15
                                                 
                                                         
        def laser_collision():
                 nonlocal player_health
                 if evade_player.hit_timer == 0:
                     if pygame.sprite.spritecollide(evade_player,laser_group,True):
                                                 
                                                 player_health-=1
                                                 evade_player.hit_timer= 5
                                                 
                                                 for i in range(1):
                                                                laser_beam=Laser_Beam.Laser_Beam()
                                                                laser_group.add(laser_beam)



        def slash():
                

                        if event.type == SLASH_EVENT:
                                sword_slash.rect.x=random.randint(10,720)
                                sword_slash.rect.y= random.randint(300,720)
                        if sword_slash.frame_index >= 3:
                                if evade_player.hit_timer == 0:
                                        if pygame.sprite.spritecollide(evade_player,sword_slash_group,False):
                                                nonlocal player_health
                                                player_health-=1
                                                evade_player.hit_timer= 15
                                        

                       



        def explode():
                                 
                          
          
                                  if event.type == EXPLODE_EVENT:
                                          bomb.rect.x=random.randint(50,650)
                                          bomb.rect.y= random.randint(300,650)
                                  if bomb.frame_index >= 3:
                                          if evade_player.hit_timer == 0:
                                                  if pygame.sprite.spritecollide(evade_player,bomb_group,False):
                                                          nonlocal player_health
                                                          player_health-=1
                                                          evade_player.hit_timer= 15

                                                  



        def punch_boundaries():
                if evade_player.rect.x > 150:
                        if keys_evade[pygame.K_RIGHT]:
                                                evade_player.rect.x -= evade_player.evade_speed
                        
                          


                                  






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

        def punch_impact_evade_phase():
            screen.fill((0,0,0))
            punch_boundaries()
            evade_player.evade_speed =20
            evade_player.rect.x = max(0, min(evade_player.rect.x, WIDTH - 50))
            evade_player.rect.y = max(300, min(evade_player.rect.y, HEIGHT - 100))
            evade_player.image= pygame.transform.scale(evade_player.image,(60,60))
            screen.blit(evade_player.image,evade_player.rect)
            screen.blit(player_shield.image,player_shield.rect)
            robot_punch.update()
            screen.blit(robot_punch.image,robot_punch.rect)
            punch_group.update()
            punch_group.draw(screen)
        def punch_wave_evade_phase():
            screen.fill((0,0,0))
            evade_player.evade_speed =10
            evade_player.rect.x = max(0, min(evade_player.rect.x, WIDTH - 50))
            evade_player.rect.y = max(400, min(evade_player.rect.y, HEIGHT - 100))
            evade_player.image= pygame.transform.scale(evade_player.image,(40,40))
            screen.blit(evade_player.image,evade_player.rect)
            
            robot_punch.update()
            screen.blit(robot_punch.image,robot_punch.rect)
            punch_wave.update()
            screen.blit(punch_wave.image,punch_wave.rect)

        def laser_evade_phase():
            screen.fill((0,0,0))
            punch_boundaries()
            screen.blit(evade_player.image,evade_player.rect)
            robot_laser.update()
            screen.blit(robot_laser.image,robot_laser.rect)
            laser_group.update()
            laser_group.draw(screen)

        def bomb_evade_phase():
            screen.fill((0,0,0))
            screen.blit(evade_player.image,evade_player.rect)
            robot_bomber.update()
            screen.blit(robot_bomber.image,robot_bomber.rect)
            bomb_group.update()
            bomb_group.draw(screen)

        def run_evade_phase():
            screen.fill((0,0,0))
            screen.blit(evade_player.image,evade_player.rect)
            robot_runner.update()
            screen.blit(robot_runner.image,robot_runner.rect)
            run_group.update()
            run_group.draw(screen)


        def neutral_phase_for_sword():
                screen.fill((0,0,0))
                screen.blit(robot_sword.image,robot_sword.rect)
                screen.blit(play_combat_button.image,play_combat_button.rect)

        def neutral_phase_for_punch():
                
                screen.fill((0,0,0))
                player_punch_1= pixel_font.render(f"PRESS 'F'", True, (255, 255, 255))
                player_punch_2= pixel_font.render(f"TO FIRE FIST", True, (255, 255, 255))
                screen.blit(player_punch_1,(450,10))
                screen.blit(player_punch_2,(450,50))
                screen.blit(robot_punch.image,robot_punch.rect)
                screen.blit(play_combat_button.image,play_combat_button.rect)

        def neutral_phase_for_laser():
                screen.fill((0,0,0))
                screen.blit(robot_laser.image,robot_laser.rect)
                screen.blit(play_combat_button.image,play_combat_button.rect)

        def neutral_phase_for_run():
                screen.fill((0,0,0))
                screen.blit(robot_runner.image,robot_runner.rect)
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

        def current_floor_text():
                nonlocal floor_number
                floor_text= pixel_font.render(f"Current Floor: {floor_number}", True, (255, 255, 255))
                screen.blit(floor_text,(10,10))


        def detect_mouse_button():
                nonlocal phase_change
                nonlocal combat_button_clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                                  if play_combat_button.rect.collidepoint(mouse_pos):
                                          if not combat_button_clicked: 
                                            combat_button_clicked = True
                                            phase_change = 1
        
                                            pygame.time.set_timer(CHANGE_PHASE_EVENT, PHASE_DURATION)

        def change_phase():
                nonlocal phase_change
                if event.type == CHANGE_PHASE_EVENT:
                        if phase_change==1:
                                phase_change=0
                        else:
                          phase_change=1
           
        def display_phase_for_sword():
                nonlocal combat_button_clicked
                nonlocal phase_change
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

        def display_phase_for_laser():
                nonlocal combat_button_clicked
                nonlocal phase_change
                if combat_button_clicked:
              
                      
                
        
                        screen.fill((0,0,0))
                        if phase_change==1:
                                        attack_phase()
                                        health_display()
                        if phase_change==0:
                                        laser_evade_phase()
                                        health_display()
                else:
                                screen.fill((0,0,0))
                                neutral_phase_for_laser()
                                health_display()

        def display_phase_for_run():
                nonlocal combat_button_clicked
                nonlocal phase_change
                if combat_button_clicked:
              
                      
                
        
                        screen.fill((0,0,0))
                        if phase_change==1:
                                        attack_phase()
                                        health_display()
                        if phase_change==0:
                                        run_evade_phase()
                                        health_display()
                else:
                                screen.fill((0,0,0))
                                neutral_phase_for_run()
                                health_display()


        def display_phase_for_punch():
                nonlocal combat_button_clicked
                nonlocal phase_change
                if combat_button_clicked:
              
                      
                
        
                        screen.fill((0,0,0))
                        if phase_change==1:
                                        attack_phase()
                                        health_display()
                        if phase_change==0:
                                        punch_impact_and_waves()
                                        health_display()
                else:
                                screen.fill((0,0,0))
                                neutral_phase_for_punch()
                                health_display()


        def display_phase_for_bomb():
                nonlocal combat_button_clicked
                nonlocal phase_change
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
                nonlocal enemy_health
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
        player_shield= Player_Shield.Player_Shield()

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
        robot_runner= Robot_Runner.Robot_Runner()
        robot_laser= Robot_Laser.Robot_Laser()
        robot_punch= Robot_Punch.Robot_Punch()

        
        punch_wave= Punch_Wave.Punch_Wave()
        sword_slash_group= pygame.sprite.Group()
        laser_group= pygame.sprite.Group()
        bomb_group = pygame.sprite.Group()
        
        run_group = pygame.sprite.Group()
        punch_group= pygame.sprite.Group()
        play_combat_button= Play_Combat.Play_Combat_Button()


        


        for i in range (3):
                punch_red=PUNCH_RED.Robot_Punch_Red()
                punch_group.add(punch_red)
        for i in range(10):
                sword_slash= Sword_Slash.Sword_Slash()
                sword_slash_group.add(sword_slash)

        for i in range(2):
                bomb=Bombs.Bombs()
                bomb_group.add(bomb)

        for i in range(1):
                robot_run=Robot_Run.Robot_Run()
                run_group.add(robot_run)

        for i in range(2):
                laser_beam=Laser_Beam.Laser_Beam()
                laser_group.add(laser_beam)

        pygame.time.set_timer(SLASH_EVENT,  2000,loops=0)
        pygame.time.set_timer(EXPLODE_EVENT,  2000,loops=0)
        pygame.time.set_timer(PUNCH_EVENT,1500,loops=0)
        pygame.time.set_timer(SWITCH_WAVES,2000,loops=0)
        pygame.time.set_timer(SWITCH_PUNCH,10000,loops=0)


        running = True



        
        while running:
        
                clock.tick(FPS)
                mouse_pos= pygame.mouse.get_pos()
                #Events
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                          running = False

                        detect_mouse_button()
                        i_frames()
                
                        change_phase()
                        shield_follow(event) 
                        change_punch_impact_and_waves()
                                        
                                    

                        if event.type == pygame.KEYDOWN:
                                keys_attack = pygame.key.get_pressed()
                                attack_player.move_attack(keys_attack) 

                        for sword_slash in sword_slash_group:
                                slash()

                        for bomb in bomb_group:
                                explode()

                for robot_run in run_group:
                                run_collision()

                for laser_beam in laser_group:
                                        laser_collision()

                        
                            
                is_shield_active()                       
                shield_collision() 
                punch_wave_collision()

                keys_evade = pygame.key.get_pressed()
                evade_player.move_evade(keys_evade)

                
                

                Enemy_Collision()

                Floor_Change_Player()
                Floor_Change_Enemy()
                if game_state== "Floor":
                     keys = pygame.key.get_pressed()
                     floor_player.move_floor(keys)
                     Floors()
                     current_floor_text()
                
        
                
        
        
                                                
        
        
                game_win()
                evade_player.update_timer()
                player_attack()
                evade_player.boudaries() 
                floor_player.boudaries()
                
                        

                pygame.display.flip()
               
                
                        
      

        pygame.quit()
